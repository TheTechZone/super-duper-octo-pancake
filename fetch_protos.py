import requests
import re
import hashlib
import pathlib
import shlex
import subprocess
import os

# Define the base URL for the GitHub Search API
base_url = "https://api.github.com/search/code"

# Define the search query parameters
query_params = {
    "q": 'repo:signalapp/Signal-Android repo:signalapp/libsignal language:"Protocol Buffer"',
    "per_page": 100,  # You can change this to navigate through pages of results
}

# Your personal access token
if os.environ.get("GITHUB_ACCESS_TOKEN") is None:
    exit("NO Github PAT provided")
token = os.environ.get("GITHUB_ACCESS_TOKEN")

# Headers to include in the request
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def request() -> list[str, str, str, str]:
    # Send the GET request to the GitHub API
    response = requests.get(base_url, params=query_params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Print the total number of results
        print(f"Total results: {data['total_count']}")

        # from json import dumps
        # with open("demo.json", "w") as f:
        #     f.write(dumps(data['items']))

        items = []

        for item in data["items"]:
            # print(f"File name: {item['name']}")
            # print(f"Hash: {item['sha']}")
            # print(f"URL: {item['html_url']}")
            # print(f"File URL: {github_to_raw(item['html_url'])}")
            # print("---")
            items.append((item["name"], item["sha"], item["html_url"]))

        return items
    else:
        print(
            f"Request failed with status code {response.status_code}: {response.text}"
        )


def github_to_raw(url):
    # Pattern to match GitHub URLs
    pattern = r"https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)"

    # Search for the pattern in the URL
    match = re.search(pattern, url)

    if match:
        # Extract the components from the URL
        owner, repo, branch, path = match.groups()

        # Construct the raw file URL
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"

        return raw_url
    else:
        raise ValueError("Invalid GitHub URL")


def get_commits():
    url_commits = "https://api.github.com/repos/signalApp/Signal-Android/commits"
    response_commits = requests.get(url_commits, headers=headers)
    commits = response_commits.json()
    for commit in commits:
        print(f"Commit: {commit['sha']}, Message: {commit['commit']['message']}")


def get_tags():
    url_tags = "https://api.github.com/repos/signalApp/Signal-Android/tags"
    response_tags = requests.get(url_tags, headers=headers)
    tags = response_tags.json()
    for tag in tags:
        print(f"Tag: {tag['name']}, Commit: {tag['commit']['sha']}")


def git_hash(content: bytes = b"Nobody inspects the spammish repetition"):
    header = f"blob {len(content)}\0".encode("utf-8")
    data = header + content
    return hashlib.sha1(data).hexdigest()


proto_dir = pathlib.Path("./protos").resolve()
proto_dir.mkdir(parents=True, exist_ok=True)


def download(url, file_name):
    # open in binary mode
    with (proto_dir / file_name).open("wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)


def update_if_newer(hash: str, fname: str, url: str):
    # check if file exists locally
    fpath = (proto_dir / fname).resolve()
    if fpath.is_file():
        # file exists, check hash
        # with fpath.open("rb") as f:
        fhash = git_hash(fpath.read_bytes())
        if fhash == hash:
            print(
                f"The file {fname} currently exists (same hash). Skipping re-download."
            )
            return

    download(github_to_raw(url), fname)


def compile_protobuf(proto_file, src_dir="protos", dst_dir="protos/gen", zipped=False):
    """
    Compiles a .proto file into Python classes.

    :param src_dir: The source directory containing the .proto file.
    :param dst_dir: The destination directory where the generated Python file will be saved.
    :param proto_file: The name of the .proto file.
    """
    # Construct the command
    cmd = f"protoc -I{src_dir} --python_out={dst_dir} {src_dir}/{proto_file}"
    print(f"[D]: running command `{cmd}`")
    args = shlex.split(cmd)

    # Execute the command
    try:
        subprocess.run(args, check=True)
        print(f"Successfully compiled {proto_file} into Python classes.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to compile {proto_file}. Error: {e}")


def compile_if_newer(hash: str, fname: str):
    fpath = (proto_dir / fname).resolve()
    if fpath.is_file():
        # file exists, check hash
        # with fpath.open("rb") as f:
        fhash = git_hash(fpath.read_bytes())
        if fhash == hash:
            print(f"The file {fname} currently exists (same hash). Skipping compile.")
            return
    compile_protobuf(fname)


assert (
    git_hash(b"what is up, doc?") == "bd9dbf5aae1a3862dd1526723246b20206e5fc37"
), "git-hash is incorrect"


items = request()
for item in items:
    fname, hash, url = item
    update_if_newer(hash, fname, url)

# this requires a second-pass since some protos import from others
exclusions = ["Database.proto"]  # todo: the protobuf file is broken. skipping
for item in items:
    fname, hash, _ = item
    if fname in exclusions:
        continue
    # compile_if_newer(hash, fname)
    compile_protobuf(fname)
