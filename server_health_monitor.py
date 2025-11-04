import paramiko
from jira import JIRA

# Connect to server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('<add server ip>', username='', password='')

stdin, stdout, stderr = ssh.exec_command("free -m | grep Mem | awk '{print $4}'")
free_mem = int(stdout.read().decode().strip())

ssh.close()

print(f"Current free memory: {free_mem}MB")

# Connect to Jira
jira = JIRA(server='https://your_jira_server.atlassian.net', basic_auth=('', '')) # add jira account email first, then api token

if free_mem < 2000:
    print("Memory is low! Creating JIRA ticket...")

    try:
        myself = jira.myself()
        my_account_id = myself['accountId']
        print(f"Your account ID: {my_account_id}")

        project = jira.project('SP')
        print(f"Project key: {project.key}")

    except Exception as e:
        print(f"Error getting user info: {e}")
        my_account_id = None

    # Ticket creation
    issue_dict = {
        'project': {'key': 'SP'},
        'issuetype': {'name': 'Task'},
        'summary': 'Memory below threshold on 10.180.2.149',
        'description': f'Memory critically low: {free_mem}MB remaining.\n\nServer: 10.180.2.149\nThreshold: 2000MB\nCurrent: {free_mem}MB',
        'priority': {'name': 'Highest'}
    }

    new_issue = jira.create_issue(fields=issue_dict)
    print("Ticket Created Successfully:", new_issue.key)

    if my_account_id:
        try:
            new_issue.update(assignee={'accountId': my_account_id})
            print("Ticket assigned to you")
        except Exception as e:
            print(f"Could not assign ticket: {e}")
    else:
        print(" Ticket created but not assigned")

    print(" Ticket URL:", f"https://add_your_jira_server.atlassian.net/browse/{new_issue.key}")

else:
    print("Memory is OK. No action needed.")
