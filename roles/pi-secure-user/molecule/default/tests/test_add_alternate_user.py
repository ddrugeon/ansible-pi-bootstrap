import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_alternate_user_exists(host):
    user = host.user("apple")
    groups = ["adm","dialout","cdrom","sudo","audio","video","plugdev","games","users","input","netdev","gpio","i2c","spi", "pi"]

    assert user.exists
    assert user.home == "/home/apple"
    assert user.shell == "/bin/sh"
    assert all(current in user.groups for current in groups)
    assert user.uid == 1001

    user = host.user("orange")
    groups = ["adm", "dialout", "cdrom", "sudo", "audio", "video", "plugdev",
              "games", "users", "input", "netdev", "gpio", "i2c", "spi", "pi"]

    assert user.exists
    assert user.home == "/home/orange"
    assert user.shell == "/bin/bash"
    assert all(current in user.groups for current in groups)
    assert user.uid == 1002
