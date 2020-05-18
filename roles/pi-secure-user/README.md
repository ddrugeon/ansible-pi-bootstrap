Ansible Role: pi-secure-user
=========
Add default sudoer user to raspberry pi, change default password for user "pi"

Requirements
------------

No special requirements; note that this role requires root access, so either run it in a playbook with a global become: yes, or invoke the role in your playbook like:

```yaml
- hosts: pi
  become: yes
  roles:
    - role: pi-secure-user
```

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

```yaml
pi_secure_user_default_shell: "/bin/bash"
```
Default bash to use for new users.

```yaml
pi_secure_user_custom_pi_password: "raspberry"
```
Default password for pi user. Note that it is the same than when booting for the first time your raspberry pi.

```yaml
pi_secure_user_alternate_users: []
```
List of users to create or update, default is []. Each item in this list should be a hash with the following keys:
- name: Username of new user (required)
- fullname: Full name for the new user (optional)
- shell: Default shell for this user; `pi_secure_user_default_shell` will be used if this key is omitted.
- pubkey: The public keys to associate with the given user.
- pubkey_options: Additional options to pass to the authorized_key module (optional).
- exclusive: Boolean indicating if all other public keys should be removed (optional)

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: pi
  become: yes
  vars:
    pi_secure_user_custom_pi_password: "{{ vaulted_custom_pi_password }}"
    pi_secure_user_alternate_users:
      - username: "orange"
        fullname: "User Orange"
        pubkey:
          - "ssh-rsa ..."
          - "ssh-rsa ..."
    pi_secure_user_alternate_user_password: "{{ vaulted_user_password }}"
  roles:
    - role: pi-secure-user
```

```

License
-------

MIT

Author Information
------------------

David Drugeon-Hamon [ddrugeon](https://github.com/ddrugeon)