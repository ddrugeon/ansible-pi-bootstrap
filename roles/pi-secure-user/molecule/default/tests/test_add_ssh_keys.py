import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize("user_home", [
    ("/home/apple"),
    ("/home/orange")
])
def test_authorized_keys_added(host, user_home):
    f = host.file(user_home+'/.ssh/authorized_keys')
    assert f.contains('Fake SSH Key only for testing purpose')
