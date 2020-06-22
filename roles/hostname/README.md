Ansible Role: hostname
=========
Change hostname on raspberry pi.

Requirements
------------

No special requirements; note that this role requires root access, so either run it in a playbook with a global become: yes, or invoke the role in your playbook like:

```yaml
- hosts: pi
  become: yes
  roles:
    - role: hostname
```

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

```yaml
hostname_value: "raspberrypi"
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: pi
  become: yes
  vars:
    hostname_value: "retropie"
  roles:
    - role: hostname
```

```

License
-------

MIT

Author Information
------------------

David Drugeon-Hamon [ddrugeon](https://github.com/ddrugeon)