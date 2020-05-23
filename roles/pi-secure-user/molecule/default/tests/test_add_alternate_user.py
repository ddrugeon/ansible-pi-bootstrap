import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

@pytest.mark.parametrize("username", [
    ("apple"),
    ("orange")
])
def test_alternate_user_exists(host, username):
    user = host.user(username)
    groups = ["adm","dialout","cdrom","sudo","audio","video","plugdev","games","users","input","netdev","gpio","i2c","spi", "pi"]

    assert user.exists
    assert all(current in user.groups for current in groups)
    assert user.home == "/home/"+username

    if username == 'apple':
        assert user.uid == 1001
        assert user.shell == "/bin/sh"
    elif username == 'orange':
        assert user.uid == 1002
        assert user.shell == "/bin/bash"
