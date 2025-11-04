from jira import JIRA
from datetime import datetime

# JIRA connection setup
user = '' # add your jira account email
apikey = '' # add your api token
server = '' # add your jira

print("Connecting to JIRA...")
jira = JIRA(server=server, basic_auth=(user, apikey))
print("Connected to JIRA successfully!")

# Create a new JIRA ticket
print("\n" + "=" * 50)
print("CREATING NEW JIRA TICKET")
print("=" * 50)

ticket_data = {
    'project': {'key': 'SP'},
    'summary': 'Test Issue Created via Python Script',
    'description': 'This is a test issue created automatically via Python JIRA REST API.',
    'issuetype': {'name': 'Task'},
}

try:
    new_ticket = jira.create_issue(fields=ticket_data)
    print("Ticket Created Successfully!")
    print(f"Ticket Key: {new_ticket.key}")
    print(f"Ticket URL: {server}/browse/{new_ticket.key}")

    # Save ticket key for later use
    ticket_key = new_ticket.key

except Exception as e:
    print(f"Error creating ticket: {e}")
    exit()

# Add comment to the ticket
print("\n" + "=" * 50)
print("ADDING COMMENT TO TICKET")
print("=" * 50)

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

comment_text = f"""
This is an automated comment added via Python script.
Timestamp: {current_time}

Additional details:
- Script: JIRA Automation
- Purpose: Testing comment functionality
- Status: In Progress
"""

try:
    comment = jira.add_comment(ticket_key, comment_text)
    print("Comment added successfully!")
    print(f"Comment ID: {comment.id}")

except Exception as e:
    print(f"Error adding comment: {e}")

#Fetch all comments from the ticket
print("\n" + "=" * 50)
print("FETCHING TICKET COMMENTS")
print("=" * 50)

try:
    issue = jira.issue(ticket_key)

    print(f"Ticket Summary: {issue.fields.summary}")
    print(f"Status: {issue.fields.status.name}")
    print(f"Reporter: {issue.fields.reporter.displayName}")
    print(f"Created: {issue.fields.created}")

    comments = jira.comments(issue)
    print(f"\nTotal Comments Found: {len(comments)}")

    for i, comment in enumerate(comments, 1):
        print(f"\n--- Comment {i} ---")
        print(f"Author: {comment.author.displayName}")
        print(f"Date: {comment.created}")
        print(f"Comment ID: {comment.id}")
        print(f"Content:\n{comment.body}")
        print("-" * 50)

except Exception as e:
    print(f"Error fetching comments: {e}")

# Display complete tickt details
print("\n" + "=" * 60)
print("COMPLETE TICKET DETAILS")
print("=" * 60)

try:
    issue = jira.issue(ticket_key)

    print(f"\nBASIC TICKET INFORMATION:")
    print(f"   Key: {issue.key}")
    print(f"   Summary: {issue.fields.summary}")
    print(f"   Description: {issue.fields.description}")
    print(f"   Status: {issue.fields.status.name}")

    if issue.fields.priority:
        print(f"   Priority: {issue.fields.priority.name}")
    else:
        print(f"   Priority: Not Set")

    print(f"   Reporter: {issue.fields.reporter.displayName}")

    if issue.fields.assignee:
        print(f"   Assignee: {issue.fields.assignee.displayName}")
    else:
        print(f"   Assignee: Unassigned")

    print(f"   Created: {issue.fields.created}")
    print(f"   Updated: {issue.fields.updated}")


except Exception as e:
    print(f"Error displaying ticket details: {e}")

print("\n" + "=" * 50)
print("COMMENTS FROM TODAY")
print("=" * 50)

try:
    today = datetime.now()
    issue = jira.issue(ticket_key)
    comments = jira.comments(issue)

    today_comments = []

    for comment in comments:
        comment_date = datetime.strptime(comment.created.split('T')[0], '%Y-%m-%d')
        if comment_date.date() == today.date():
            today_comments.append(comment)

    print(f"Comments from {today.date()}: {len(today_comments)}")

    for i, comment in enumerate(today_comments, 1):
        print(f"\n--- Today's Comment {i} ---")
        print(f"Author: {comment.author.displayName}")
        print(f"Date: {comment.created}")
        print(f"Content:\n{comment.body}")
        print("-" * 50)

except Exception as e:
    print(f"Error fetching today's comments: {e}")

print("\n" + "=" * 50)
print("SCRIPT COMPLETED SUCCESSFULLY!")
print("=" * 50)