
# Load data from files
class InputText(luigi.ExternalTask):
    """
    This class represents something that was created elsewhere by an external process,
    so all we want to do is to implement the output method.
    """
    filename = luigi.Parameter()

    def output(self):
        """
        Returns the target output for this task.
        In this case, it expects a file to be present in the local file system.
        :return: the target output for this task.
        :rtype: object (:py:class:`luigi.target.Target`)
        """

        # The directory containing this file
        root = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/"
        return luigi.LocalTarget(root + self.filename)
