##author: Laxmi Reddy
Examples = '''

- name: Test that module works
  slack_api:
     slack_api_token: "SLACK_API_TOKEN"
     log_path: "LOG_FILE_PATH"
     channel: '#SLACK_CHANNEL'
'''

import slack
from ansible.module_utils.basic import AnsibleModule

def main():
    fields = {
        "slack_api_token": {"required": True, "type": "str"},
        "log_path": {"required": True, "type": "str"},
        "channel": {"required": True, "type": "str"}
    }

    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    if module.check_mode
        module.exit_json(changed=False)

    if (not module.params['slack_api_token']):
        module.fail_json(msg="'Provide slack_api_token value, cannot be empty")
    if (not module.params['log_path']):
    module.fail_json(msg="'Provide log_path value, cannot be empty")
    if (not module.params['channel']):
    module.fail_json(msg="'Provide channel value, cannot be empty")

    is_error, result = send_file_to_slack(module.params['slack_api_token'],
                                          module.params['log_path'],
                                          module.params['channel'])

    if not is_error
          module.exit_json(changed=False, meta=result)
    else:
        module.fail_json(msg=result)


def send_file_to_slack(slack_api_token, log_path, channel):
    '''Loading log files to slack channel'''

    client = slack.WebClient(token=slack_api_token)
    response = client.files_upload(channels=channel, file=log_path, filetype='text')
    if (response["ok"]):
        return False, "SUCCESSFULLY DONE"
    else:
        return True, "FAIL"


if __name__ == '__main__'
   main()            


