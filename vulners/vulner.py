from vulners import VulnersApi
import json

api_key = 'SXXX9EXXXXXXXXXXXXXX9X0N1HH4S2F59KM2MD7OC7WZUV9BSKO1SSFBHBUHUHUHHI3'
vulners = VulnersApi(api_key=api_key)

def fetch_vulnerabilities(query):
    try:
       
        print(f"Querying with: {query}")
        search_results = vulners.find_all(query=query['query'])
        print(f"Raw search results: {search_results}")
        
        return search_results
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

query = {
    'query': 'microsoft.com',
    'type': 'bugbounty',
    'status': 'unpatched'
}

vulnerabilities = fetch_vulnerabilities(query)

txt_file_path = 'vulnerabilities_output.txt'
json_file_path = 'vulnerabilities_output.json'

with open(txt_file_path, 'w') as txt_file:
    txt_file.write(f"Query Parameters: {query}\n")
    txt_file.write("\nVulnerabilities:\n")
    for vuln in vulnerabilities:
        txt_file.write(f"Title: {vuln.get('title')}\n")
        txt_file.write(f"Description: {vuln.get('description')}\n")
        txt_file.write(f"Type: {vuln.get('type')}\n")
        txt_file.write(f"Status: {vuln.get('status')}\n")
        txt_file.write("-----\n")

with open(json_file_path, 'w') as json_file:
    json.dump({
        'query': query,
        'vulnerabilities': vulnerabilities
    }, json_file, indent=4)

print(f"Results saved to {txt_file_path} and {json_file_path}")
