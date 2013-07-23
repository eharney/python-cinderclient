from cinderclient.tests import utils
from cinderclient.tests.v1 import fakes


cs = fakes.FakeClient()


class SnapshotActionsTest(utils.TestCase):
    def test_finalize_snapshot_metadata(self):
        s = cs.volume_snapshots.get('1234')
        cs.volume_snapshots.finalize_snapshot_metadata(s, 'available')
        cs.assert_called('POST', '/snapshots/1234/action')

    def test_delete_snapshot_metadata(self):
        s = cs.volume_snapshots.get('1234')
        cs.volume_snapshots.delete_snapshot_metadata(s)
        cs.assert_called('POST', '/snapshots/1234/action')
