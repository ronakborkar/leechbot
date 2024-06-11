#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'copy{CMD_SUFFIX}', f'c{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbcopy{CMD_SUFFIX}', f'qc{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl{CMD_SUFFIX}', f'yd{CMD_SUFFIX}']
        self.LeechCommand = [f'download{CMD_SUFFIX}', f'd{CMD_SUFFIX}']
        self.QbLeechCommand = [f'torrentD{CMD_SUFFIX}', f'qD{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdwd{CMD_SUFFIX}', f'yd{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'unzipcopy{CMD_SUFFIX}', f'uzc{CMD_SUFFIX}', f'zipcopy{CMD_SUFFIX}', f'zc{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'qbunzipcopy{CMD_SUFFIX}', f'quzc{CMD_SUFFIX}', f'qbzipcopy{CMD_SUFFIX}', f'qzc{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'ytdlzip{CMD_SUFFIX}', f'yz{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'unzipdwld{CMD_SUFFIX}', f'uzd{CMD_SUFFIX}', f'zipdwld{CMD_SUFFIX}', f'zd{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'qbunzipdwld{CMD_SUFFIX}', f'quzd{CMD_SUFFIX}', f'qbzipdwld{CMD_SUFFIX}', f'qzd{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'ytdlzipdwld{CMD_SUFFIX}', f'yzd{CMD_SUFFIX}'])
        self.CloneCommand = [f'clone{CMD_SUFFIX}', f'c{CMD_SUFFIX}']
        self.CountCommand = f'count{CMD_SUFFIX}'
        self.DeleteCommand = f'del{CMD_SUFFIX}'
        self.CancelMirror = f'cancel{CMD_SUFFIX}'
        self.CancelAllCommand = [f'cancelall{CMD_SUFFIX}', 'cancellallbot']
        self.ListCommand = f'list{CMD_SUFFIX}'
        self.SearchCommand = f'search{CMD_SUFFIX}'
        self.StatusCommand = [f'status{CMD_SUFFIX}', f's{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorize{CMD_SUFFIX}', f'a{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorize{CMD_SUFFIX}', f'ua{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklist{CMD_SUFFIX}', f'bl{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklist{CMD_SUFFIX}', f'rbl{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'ping{CMD_SUFFIX}', f'p{CMD_SUFFIX}']
        self.RestartCommand = [f'restart{CMD_SUFFIX}', f'r{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats{CMD_SUFFIX}', f'st{CMD_SUFFIX}']
        self.HelpCommand = f'help{CMD_SUFFIX}'
        self.LogCommand = f'log{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = [f'bsetting{CMD_SUFFIX}', f'bs{CMD_SUFFIX}']
        self.UserSetCommand = [f'usetting{CMD_SUFFIX}', f'us{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel{CMD_SUFFIX}'
        self.CategorySelect = f'ctsel{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtest{CMD_SUFFIX}', f'sp{CMD_SUFFIX}']
        self.RssCommand = f'rss{CMD_SUFFIX}'
        self.LoginCommand = 'login'
        self.AddImageCommand = f'addimg{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.IMDBCommand = f'imdb{CMD_SUFFIX}'
        self.AniListCommand = f'anime{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelp{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mediainfo{CMD_SUFFIX}', f'mi{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdl{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gdclean{CMD_SUFFIX}', f'gc{CMD_SUFFIX}']
        self.BroadcastCommand = [f'broadcast{CMD_SUFFIX}', f'bc{CMD_SUFFIX}']

BotCommands = _BotCommands()
