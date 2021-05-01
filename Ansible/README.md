# DevOps

Ansible Glossary

The following Ansible-specific terms are largely used throughout this guide:

Control Machine / Node: a system where Ansible is installed and configured to connect and execute commands on nodes.

Node: a server controlled by Ansible.

Inventory File: a file that contains information about the servers Ansible controls, typically located at /etc/ansible/hosts or custom inventory files as shown in env folder

Playbook: a file containing a series of tasks to be executed on a remote server.
Role: a collection of playbooks and other files that are relevant to a goal such as installing a web server.

Play: a full Ansible run. A play can have several playbooks and roles, included from a single playbook that acts as entry point.
