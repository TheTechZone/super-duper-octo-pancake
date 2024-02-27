import yaml
from json import dumps
import re


def parse_openapi_spec(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def generate_python_code(spec):
    code_snippets = [
        "from mitmproxy.http import HTTPFlow\n"
        "from xepor import InterceptedAPI, RouteType\n\n"
        f"{get_servers(spec)}\n"
        "api = InterceptedAPI(HOST_HTTPBIN)\n\n"
    ]
    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            endpoint_code = f"@api.route('{path}', methods=['{method.upper()}'])\n"
            endpoint_code += f"{build_signature(path, details)}\n"
            endpoint_code += f"    '''\n\t{details.get('summary', '')}\n\t{details.get('description','')}\n"
            endpoint_code += f"     Parameters:\n{get_params(details)}\n\n"
            endpoint_code += f"     Responses:\n{get_responses(details)}\n\n"
            endpoint_code += f"     {get_security(spec, details)}\n"
            endpoint_code += "      '''\n"
            endpoint_code += "    # Implement the function body here\n"
            endpoint_code += "    pass\n\n"
            code_snippets.append(endpoint_code)
            # break
        # break
    code_snippets.append("ddons = [api]")
    return "\n".join(code_snippets)


def build_signature(path, details):
    args = get_route_args(path)
    args_str = ", ".join(args)
    return f"def {path.replace('/', '_').replace('-','_').replace('{','').replace('}','').lstrip('_')}(flow: HTTPFlow{','+args_str if len(args) > 0 else ''}):"


def get_servers(spec, main="PRODUCTION"):
    svrs = []
    for server in spec.get("servers"):
        svrs.append(
            f'SIGNAL_{server.get("description").split()[0].upper()}_SERVER="{server.get("url")}"'
        )

    svrs.append(f'HOST_HTTPBIN="SIGNAL_{main}_SERVER"')
    return "\n".join(svrs)


def get_params(details, indent=8):
    resp = []
    for param in details.get("parameters", []):
        # resp.append(code)
        name, loc, desc, req = (
            param.get("name"),
            param.get("in"),
            param.get("description"),
            param.get("required"),
        )
        resp.append(f"{' '*indent}{name}{ '  (required)' if req else ''}")
        resp.append(f"{' '*indent}  location: {loc}")
        resp.append(f"{' '*indent}  {desc}\n")
        # resp.append(f"{' '*indent}{code} - {details['responses'][code]['description']}")
    return "\n".join(resp)


def get_responses(details, indent=8):
    resp = []
    for code in details.get("responses"):
        # resp.append(code)
        desc = details["responses"][code].get("description", "")
        resp.append(f"{' '*indent}{code} - {desc}")
    return "\n".join(resp)


def get_security(spec, details, indent=8):
    res = []
    for sec in details.get("security", []):
        if sec == {}:
            continue
        for key in sec.keys():
            res.append(
                f"{' '*indent}{key} - {spec['components']['securitySchemes'][key]['scheme']}\n{' '*(indent)}{spec['components']['securitySchemes'][key]['description']}"
            )
    if len(res) > 0:
        res.insert(0, f"Security:")
    return "\n".join(res)


def get_route_args(path: str) -> list[str]:
    # Regular expression pattern to find text inside curly braces
    pattern = r"\{([^}]*)\}"

    # Find all matches
    matches = re.findall(pattern, path)

    return [match for match in matches]


def main():
    # Step  1: Parse the OpenAPI YAML file
    spec = parse_openapi_spec("signal-server-openapi.yaml")

    # Step  2: Generate Python code
    python_code = generate_python_code(spec)

    # Output the generated code
    with open("server_proto.py", "w") as f:
        f.write(python_code)

if __name__ == "__main__":
    main()
