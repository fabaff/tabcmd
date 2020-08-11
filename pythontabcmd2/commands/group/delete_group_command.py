from ..commands import Commands
from .group_command import GroupCommand
from .. import DeleteGroupParser
import tableauserverclient as TSC
from .. import log


class DeleteGroupCommand(GroupCommand):
    def __init__(self, args):
        super().__init__(args)
        self.logger = log('pythontabcmd2.delete_group_command',
                          self.logging_level)

    @classmethod
    def parse(cls):
        args = DeleteGroupParser.delete_group_parser()
        return cls(args)

    def run_command(self):
        server_object = Commands.deserialize()
        self.delete_group(server_object)

    def delete_group(self, server):
        """Method to delete group using Tableauserverclient methods"""
        try:
            group_id = GroupCommand.find_group_id(server, self.name)
            server.groups.delete(group_id)
            self.logger.info("Successfully deleted group")
        except TSC.ServerResponseError as e:
            self.logger.error("Server error occurred", e)

