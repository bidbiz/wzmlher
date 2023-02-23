from bot import CMD_SUFFIX
from os import environ

def getCommand(name: str, command: str):
    try:
        if len(environ[name]) == 0:
            raise KeyError
        return environ[name]
    except KeyError:
        return command

class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand(f'START_COMMAND', f'start6{CMD_SUFFIX}')
        self.MirrorCommand = getCommand(f'MIRROR_COMMAND', f'mirror6{CMD_SUFFIX}'), f'm6{CMD_SUFFIX}'
        self.UnzipMirrorCommand = getCommand(f'UNZIP_COMMAND', f'unzipmirror6{CMD_SUFFIX}'), f'uzm6{CMD_SUFFIX}'
        self.ZipMirrorCommand = getCommand(f'ZIP_COMMAND', f'zipmirror6{CMD_SUFFIX}'), f'zm6{CMD_SUFFIX}'
        self.LeechCommand = getCommand(f'LEECH_COMMAND', f'leech6{CMD_SUFFIX}'), f'l6{CMD_SUFFIX}'
        self.UnzipLeechCommand = getCommand(f'UNZIPLEECH_COMMAND', f'unzipleech6{CMD_SUFFIX}'), f'uzl6{CMD_SUFFIX}'
        self.ZipLeechCommand = getCommand(f'ZIPLEECH_COMMAND', f'zipleech6{CMD_SUFFIX}'), f'zl6{CMD_SUFFIX}'
        self.CloneCommand = getCommand(f'CLONE_COMMAND', f'clone6{CMD_SUFFIX}'), f'c{CMD_SUFFIX}'
        self.QbMirrorCommand = getCommand(f'QBMIRROR_COMMAND', f'qbmirror6{CMD_SUFFIX}'), f'qm6{CMD_SUFFIX}'
        self.QbUnzipMirrorCommand = getCommand(f'QBUNZIP_COMMAND', f'qbunzipmirror6{CMD_SUFFIX}'), f'quzm6{CMD_SUFFIX}'
        self.QbZipMirrorCommand = getCommand(f'QBZIP_COMMAND', f'qbzipmirror6{CMD_SUFFIX}'), f'qzm6{CMD_SUFFIX}'
        self.QbLeechCommand = getCommand(f'QBLEECH_COMMAND', f'qbleech6{CMD_SUFFIX}'), f'ql6{CMD_SUFFIX}'
        self.QbUnzipLeechCommand = getCommand(f'QBZIPLEECH_COMMAND', f'qbunzipleech6{CMD_SUFFIX}'), f'quzl6{CMD_SUFFIX}'
        self.QbZipLeechCommand = getCommand(f'QBUNZIPLEECH_COMMAND', f'qbzipleech6{CMD_SUFFIX}'), f'qzl6{CMD_SUFFIX}'
        self.ScrapeCommand = getCommand(f'SCRAPE_COMMAND', f'scrape6{CMD_SUFFIX}'), f'sm6{CMD_SUFFIX}'
        self.YtdlCommand =  getCommand(f'YTDL_COMMAND', f'ytdl6{CMD_SUFFIX}'), f'y6{CMD_SUFFIX}'
        self.YtdlZipCommand = getCommand(f'YTDLZIP_COMMAND', f'ytdlzip6{CMD_SUFFIX}'), f'yz6{CMD_SUFFIX}'
        self.YtdlLeechCommand = getCommand(f'YTDLLEECH_COMMAND',  f'ytdlleech6{CMD_SUFFIX}'), f'yl6{CMD_SUFFIX}'
        self.YtdlZipLeechCommand = getCommand(f'YTDLZIPLEECH_COMMAND', f'ytdlzipleech6{CMD_SUFFIX}'), f'yzl6{CMD_SUFFIX}'
        self.MediaInfoCommand = getCommand(f'MEDIAINFO_COMMAND', f'mediainfo6{CMD_SUFFIX}'), f'mi6{CMD_SUFFIX}'
        self.UserSetCommand  = getCommand(f'USERSET_COMMAND', f'usetting6{CMD_SUFFIX}'), f'us6{CMD_SUFFIX}'
        self.BotSetCommand = getCommand(f'BOT_SETTING', f'bsetting6{CMD_SUFFIX}'), f'bs6{CMD_SUFFIX}'
        self.CancelMirror = getCommand(f'CANCEL_COMMAND', f'cancel6{CMD_SUFFIX}')
        self.CancelAllCommand = getCommand(f'CANCEL_ALL_COMMAND', f'cancelall6{CMD_SUFFIX}')
        self.ListCommand = getCommand(f'LIST_COMMAND', f'list6{CMD_SUFFIX}')
        self.SearchCommand = getCommand(f'SEARCH_COMMAND', f'search6{CMD_SUFFIX}')
        self.StatusCommand = getCommand(f'STATUS_COMMAND', f'status6{CMD_SUFFIX}')
        self.UsersCommand = getCommand(f'USERS_COMMAND', f'users6{CMD_SUFFIX}')
        self.PaidUsersCommand = getCommand(f'PAID_COMMAND', f'paid6{CMD_SUFFIX}')
        self.AddPaidCommand = getCommand(f'ADDPAID_COMMAND', f'addpaid6{CMD_SUFFIX}')
        self.RmPaidCommand = getCommand(f'RMPAID_COMMAND', f'rmpaid6{CMD_SUFFIX}')
        self.AuthorizeCommand = getCommand(f'AUTH_COMMAND', f'authorize6{CMD_SUFFIX}')
        self.UnAuthorizeCommand = getCommand(f'UNAUTH_COMMAND', f'unauthorize6{CMD_SUFFIX}')
        self.AddSudoCommand = getCommand(f'ADDSUDO_COMMAND', f'addsudo6{CMD_SUFFIX}')
        self.RmSudoCommand = getCommand(f'RMSUDO_COMMAND', f'rmsudo6{CMD_SUFFIX}')
        self.PingCommand = getCommand(f'PING_COMMAND', f'ping6{CMD_SUFFIX}')
        self.RestartCommand =  getCommand(f'RESTART_COMMAND', f'restart6{CMD_SUFFIX}')
        self.StatsCommand = getCommand(f'STATS_COMMAND', f'stats6{CMD_SUFFIX}')
        self.HelpCommand = getCommand(f'HELP_COMMAND', f'help6{CMD_SUFFIX}')
        self.LogCommand = getCommand(f'LOG_COMMAND', f'log6{CMD_SUFFIX}')
        self.BtSelectCommand = getCommand(f'BTSEL_COMMAND', f'btsel6{CMD_SUFFIX}')
        self.SpeedCommand = getCommand(f'SPEEDTEST_COMMAND', f'speedtest6{CMD_SUFFIX}'), f'st6{CMD_SUFFIX}'
        self.CountCommand = getCommand(f'COUNT_COMMAND', f'count6{CMD_SUFFIX}')
        self.DeleteCommand = getCommand(f'DELETE_COMMAND', f'del6{CMD_SUFFIX}')
        self.ShellCommand = getCommand(f'SHELL_COMMAND', f'shell6{CMD_SUFFIX}')
        self.ExecHelpCommand = getCommand(f'EXEHELP_COMMAND', f'exechelp6{CMD_SUFFIX}')
        self.HashCommand = getCommand(f'HASH_COMMAND', f'hash6{CMD_SUFFIX}')
        self.RssListCommand = getCommand(f'RSSLIST_COMMAND', f'rsslist6{CMD_SUFFIX}')
        self.RssGetCommand = getCommand(f'RSSGET_COMMAND', f'rssget6{CMD_SUFFIX}')
        self.RssSubCommand = getCommand(f'RSSSUB_COMMAND', f'rsssub6{CMD_SUFFIX}')
        self.RssUnSubCommand = getCommand(f'RSSUNSUB_COMMAND', f'rssunsub6{CMD_SUFFIX}')
        self.RssSettingsCommand = getCommand(f'RSSSET_COMMAND', f'rssset6{CMD_SUFFIX}')
        self.WayBackCommand = getCommand(f'WAYBACK_COMMAND', f'wayback6{CMD_SUFFIX}')
        self.AddleechlogCommand = getCommand(f'ADDLEECHLOG_CMD', f'addleechlog6{CMD_SUFFIX}')
        self.RmleechlogCommand = getCommand(f'RMLEECHLOG_CMD', f'rmleechlog6{CMD_SUFFIX}')
        self.SelectCategory = getCommand(f'CATSEL_CMD', f'catsel6{CMD_SUFFIX}')
        self.EvalCommand = f'eval6{CMD_SUFFIX}'
        self.ExecCommand = f'exec6{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals6{CMD_SUFFIX}'

BotCommands = _BotCommands()
