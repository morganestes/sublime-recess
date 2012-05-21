import sublime_plugin


class RecessCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('set_build_system', {
          'file': 'Packages/Twitter Recess/Recess.sublime-build'
        })
        self.window.run_command('build')
