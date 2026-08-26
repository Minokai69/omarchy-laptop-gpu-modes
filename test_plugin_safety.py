from pathlib import Path
import unittest


ROOT = Path(__file__).parent
PANEL = (ROOT / "Panel.qml").read_text()
README = (ROOT / "README.md").read_text()


class PluginSafetyTests(unittest.TestCase):
    def test_mode_changes_do_not_execute_user_owned_privileged_helper(self):
        self.assertNotIn('"pkexec"', PANEL)
        self.assertNotIn("gpuModeHelper", PANEL)
        self.assertIn('"supergfxctl", "-m"', PANEL)
        self.assertFalse((ROOT / "set-mode.sh").exists())

    def test_gpu_controls_are_capability_gated(self):
        self.assertIn("gpuAvailable", PANEL)
        self.assertIn("gpuVendor", PANEL)
        self.assertIn("supergfxctl -V", PANEL)
        self.assertIn("supergfxctl -s", PANEL)
        self.assertIn("visible: root.gpuAvailable", PANEL)

    def test_documentation_does_not_require_jq_or_privileged_config_rewrites(self):
        self.assertNotIn("jq", README)
        self.assertNotIn("pkexec", README)
        self.assertNotIn("/etc/supergfxd.conf", README)
        self.assertIn("supergfxctl", README)


if __name__ == "__main__":
    unittest.main()
