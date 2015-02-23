__title__ = 'DonatorRank'
__author__ = 'Jakkee'
__version__ = '1.4.1'
 
import clr
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Fougerite")
import System
import math
import Fougerite
import UnityEngine
 
 
class DonatorRank:
    def On_PluginInit(self):
        Util.ConsoleLog(__title__ + " by " + __author__ + " Version: " + __version__ + " loaded.", False)
        if not Plugin.IniExists("Settings"):
            Plugin.CreateIni("Settings")
            ini = Plugin.GetIni("Settings")
            ini.AddSetting("Settings", "JoinMessages", "true")
            ini.AddSetting("Settings", "LeaveMessages", "true")
            ini.AddSetting("Settings", "ChatPrefix", "true")
            ini.AddSetting("Settings", "OwnerSteamID", "76561198135558142")
            ini.AddSetting("Settings", "OwnerColour", "[color cyan]")
            ini.AddSetting("Settings", "AdminColour", "[color cyan]")
            ini.AddSetting("Settings", "LogTps", "true")
            ini.AddSetting("Settings", "LogKicks", "true")
            ini.AddSetting("Settings", "LogBroadcast", "true")
            ini.AddSetting("Settings", "PlayerSetHome", "Only works with HomeSystem installed (This line is not a setting)")
            ini.AddSetting("Settings", "PlayerMaxhomes", "1")
            ini.AddSetting("ModSettings", "ModeratorColour", "[color white]")
            ini.AddSetting("ModSettings", "Maxhomes", "3")
            ini.AddSetting("DonatorSettings", "DonatorColour", "[color white]")
            ini.AddSetting("DonatorSettings", "Maxhomes", "3")
            ini.AddSetting("DonatorSettings", "LVL1KitCooldown", "80000")
            ini.AddSetting("DonatorSettings", "LVL2KitCooldown", "80000")
            ini.AddSetting("DonatorSettings", "TPCooldown", "20000")
            ini.AddSetting("VIPSettings", "VIPColour", "[color white]")
            ini.AddSetting("VIPSettings", "Maxhomes", "2")
            ini.AddSetting("VIPSettings", "LVL1KitCooldown", "120000")
            ini.AddSetting("VIPSettings", "LVL2KitCooldown", "120000")
            ini.AddSetting("VIPSettings", "TPCooldown", "30000")
            ini.AddSetting("VKIT_Level1", "Inv1", "P250")
            ini.AddSetting("VKIT_Level1", "Qty1", "1")
            ini.AddSetting("VKIT_Level1", "Inv2", "9mm Ammo")
            ini.AddSetting("VKIT_Level1", "Qty2", "50")
            ini.AddSetting("VKIT_Level1", "Inv3", "Leather Helmet")
            ini.AddSetting("VKIT_Level1", "Qty3", "1")
            ini.AddSetting("VKIT_Level1", "Inv4", "Cloth Vest")
            ini.AddSetting("VKIT_Level1", "Qty4", "1")
            ini.AddSetting("VKIT_Level1", "Inv5", "Cloth Pants")
            ini.AddSetting("VKIT_Level1", "Qty5", "1")
            ini.AddSetting("VKIT_Level1", "Inv6", "Leather Boots")
            ini.AddSetting("VKIT_Level1", "Qty6", "1")
            ini.AddSetting("VKIT_Level1", "Inv7", "Large Medkit")
            ini.AddSetting("VKIT_Level1", "Qty7", "3")
            ini.AddSetting("VKIT_Level1", "Inv8", "Small Rations")
            ini.AddSetting("VKIT_Level1", "Qty8", "1")
            ini.AddSetting("VKIT_Level1", "Inv9", "Silencer")
            ini.AddSetting("VKIT_Level1", "Qty9", "1")
            ini.AddSetting("VKIT_Level1", "Inv10", "")
            ini.AddSetting("VKIT_Level1", "Qty10", "")
            ini.AddSetting("VKIT_Level2", "Inv1", "P250")
            ini.AddSetting("VKIT_Level2", "Qty1", "1")
            ini.AddSetting("VKIT_Level2", "Inv2", "9mm Ammo")
            ini.AddSetting("VKIT_Level2", "Qty2", "50")
            ini.AddSetting("VKIT_Level2", "Inv3", "Leather Helmet")
            ini.AddSetting("VKIT_Level2", "Qty3", "1")
            ini.AddSetting("VKIT_Level2", "Inv4", "Cloth Vest")
            ini.AddSetting("VKIT_Level2", "Qty4", "1")
            ini.AddSetting("VKIT_Level2", "Inv5", "Cloth Pants")
            ini.AddSetting("VKIT_Level2", "Qty5", "1")
            ini.AddSetting("VKIT_Level2", "Inv6", "Leather Boots")
            ini.AddSetting("VKIT_Level2", "Qty6", "1")
            ini.AddSetting("VKIT_Level2", "Inv7", "Large Medkit")
            ini.AddSetting("VKIT_Level2", "Qty7", "3")
            ini.AddSetting("VKIT_Level2", "Inv8", "Small Rations")
            ini.AddSetting("VKIT_Level2", "Qty8", "1")
            ini.AddSetting("VKIT_Level2", "Inv9", "Silencer")
            ini.AddSetting("VKIT_Level2", "Qty9", "1")
            ini.AddSetting("VKIT_Level2", "Inv10", "")
            ini.AddSetting("VKIT_Level2", "Qty10", "")
            ini.AddSetting("DKIT_Level1", "Inv1", "M4")
            ini.AddSetting("DKIT_Level1", "Qty1", "1")
            ini.AddSetting("DKIT_Level1", "Inv2", "556 Ammo")
            ini.AddSetting("DKIT_Level1", "Qty2", "90")
            ini.AddSetting("DKIT_Level1", "Inv3", "Leather Helmet")
            ini.AddSetting("DKIT_Level1", "Qty3", "1")
            ini.AddSetting("DKIT_Level1", "Inv4", "Leather Vest")
            ini.AddSetting("DKIT_Level1", "Qty4", "1")
            ini.AddSetting("DKIT_Level1", "Inv5", "Leather Pants")
            ini.AddSetting("DKIT_Level1", "Qty5", "1")
            ini.AddSetting("DKIT_Level1", "Inv6", "Leather Boots")
            ini.AddSetting("DKIT_Level1", "Qty6", "1")
            ini.AddSetting("DKIT_Level1", "Inv7", "Silencer")
            ini.AddSetting("DKIT_Level1", "Qty7", "1")
            ini.AddSetting("DKIT_Level1", "Inv8", "Large Medkit")
            ini.AddSetting("DKIT_Level1", "Qty8", "5")
            ini.AddSetting("DKIT_Level1", "Inv9", "Small Rations")
            ini.AddSetting("DKIT_Level1", "Qty9", "10")
            ini.AddSetting("DKIT_Level1", "Inv10", "")
            ini.AddSetting("DKIT_Level1", "Qty10", "")
            ini.AddSetting("DKIT_Level2", "Inv1", "M4")
            ini.AddSetting("DKIT_Level2", "Qty1", "1")
            ini.AddSetting("DKIT_Level2", "Inv2", "556 Ammo")
            ini.AddSetting("DKIT_Level2", "Qty2", "90")
            ini.AddSetting("DKIT_Level2", "Inv3", "Leather Helmet")
            ini.AddSetting("DKIT_Level2", "Qty3", "1")
            ini.AddSetting("DKIT_Level2", "Inv4", "Leather Vest")
            ini.AddSetting("DKIT_Level2", "Qty4", "1")
            ini.AddSetting("DKIT_Level2", "Inv5", "Leather Pants")
            ini.AddSetting("DKIT_Level2", "Qty5", "1")
            ini.AddSetting("DKIT_Level2", "Inv6", "Leather Boots")
            ini.AddSetting("DKIT_Level2", "Qty6", "1")
            ini.AddSetting("DKIT_Level2", "Inv7", "Silencer")
            ini.AddSetting("DKIT_Level2", "Qty7", "1")
            ini.AddSetting("DKIT_Level2", "Inv8", "Large Medkit")
            ini.AddSetting("DKIT_Level2", "Qty8", "5")
            ini.AddSetting("DKIT_Level2", "Inv9", "Small Rations")
            ini.AddSetting("DKIT_Level2", "Qty9", "10")
            ini.AddSetting("DKIT_Level2", "Inv10", "")
            ini.AddSetting("DKIT_Level2", "Qty10", "")
            ini.Save()
        DataStore.Flush("DonatorRank")
        DataStore.Flush("ModBan")
        ini = Plugin.GetIni("Settings")
        #DataStore.Add("DonatorRank", "VKIT1_INV1", ini.GetSetting("VKIT_Level1", "Inv1"))
        #DataStore.Add("DonatorRank", "VKIT1_INV2", ini.GetSetting("VKIT_Level1", "Inv2"))
        #DataStore.Add("DonatorRank", "VKIT1_INV3", ini.GetSetting("VKIT_Level1", "Inv3"))
        #DataStore.Add("DonatorRank", "VKIT1_INV4", ini.GetSetting("VKIT_Level1", "Inv4"))
        #DataStore.Add("DonatorRank", "VKIT1_INV5", ini.GetSetting("VKIT_Level1", "Inv5"))
        #DataStore.Add("DonatorRank", "VKIT1_INV6", ini.GetSetting("VKIT_Level1", "Inv6"))
        #DataStore.Add("DonatorRank", "VKIT1_INV7", ini.GetSetting("VKIT_Level1", "Inv7"))
        #DataStore.Add("DonatorRank", "VKIT1_INV8", ini.GetSetting("VKIT_Level1", "Inv8"))
        #DataStore.Add("DonatorRank", "VKIT1_INV9", ini.GetSetting("VKIT_Level1", "Inv9"))
        #DataStore.Add("DonatorRank", "VKIT1_INV10", ini.GetSetting("VKIT_Level1", "Inv10"))
        #DataStore.Add("DonatorRank", "VKIT1_QTY1", ini.GetSetting("VKIT_Level1", "Qty1"))
        #DataStore.Add("DonatorRank", "VKIT1_QTY2", ini.GetSetting("VKIT_Level1", "Qty2"))
        #DataStore.Add("DonatorRank", "VKIT1_QTY3", ini.GetSetting("VKIT_Level1", "Qty3"))
        #DataStore.Add("DonatorRank", "VKIT1_QTY4", ini.GetSetting("VKIT_Level1", "Qty4"))
        #DataStore.Add("DonatorRank", "VKIT1_QTY5", ini.GetSetting("VKIT_Level1", "Qty5"))
        #DataStore.Add("DonatorRank", "VKIT1_QTY6", ini.GetSetting("VKIT_Level1", "Qty6"))
        #DataStore.Add("DonatorRank", "VKIT1_QTY7", ini.GetSetting("VKIT_Level1", "Qty7"))
        #DataStore.Add("DonatorRank", "VKIT1_QTY8", ini.GetSetting("VKIT_Level1", "Qty8"))
        #DataStore.Add("DonatorRank", "VKIT1_QTY9", ini.GetSetting("VKIT_Level1", "Qty9"))
        #DataStore.Add("DonatorRank", "VKIT1_QTY10", ini.GetSetting("VKIT_Level1", "Qty10"))
        #DataStore.Add("DonatorRank", "VKIT2_INV1", ini.GetSetting("VKIT_Level2", "Inv1"))
        #DataStore.Add("DonatorRank", "VKIT2_INV2", ini.GetSetting("VKIT_Level2", "Inv2"))
        #DataStore.Add("DonatorRank", "VKIT2_INV3", ini.GetSetting("VKIT_Level2", "Inv3"))
        #DataStore.Add("DonatorRank", "VKIT2_INV4", ini.GetSetting("VKIT_Level2", "Inv4"))
        #DataStore.Add("DonatorRank", "VKIT2_INV5", ini.GetSetting("VKIT_Level2", "Inv5"))
        #DataStore.Add("DonatorRank", "VKIT2_INV6", ini.GetSetting("VKIT_Level2", "Inv6"))
        #DataStore.Add("DonatorRank", "VKIT2_INV7", ini.GetSetting("VKIT_Level2", "Inv7"))
        #DataStore.Add("DonatorRank", "VKIT2_INV8", ini.GetSetting("VKIT_Level2", "Inv8"))
        #DataStore.Add("DonatorRank", "VKIT2_INV9", ini.GetSetting("VKIT_Level2", "Inv9"))
        #DataStore.Add("DonatorRank", "VKIT2_INV10", ini.GetSetting("VKIT_Level2", "Inv10"))
        #DataStore.Add("DonatorRank", "VKIT2_QTY1", ini.GetSetting("VKIT_Level2", "Qty1"))
        #DataStore.Add("DonatorRank", "VKIT2_QTY2", ini.GetSetting("VKIT_Level2", "Qty2"))
        #DataStore.Add("DonatorRank", "VKIT2_QTY3", ini.GetSetting("VKIT_Level2", "Qty3"))
        #DataStore.Add("DonatorRank", "VKIT2_QTY4", ini.GetSetting("VKIT_Level2", "Qty4"))
        #DataStore.Add("DonatorRank", "VKIT2_QTY5", ini.GetSetting("VKIT_Level2", "Qty5"))
        #DataStore.Add("DonatorRank", "VKIT2_QTY6", ini.GetSetting("VKIT_Level2", "Qty6"))
        #DataStore.Add("DonatorRank", "VKIT2_QTY7", ini.GetSetting("VKIT_Level2", "Qty7"))
        #DataStore.Add("DonatorRank", "VKIT2_QTY8", ini.GetSetting("VKIT_Level2", "Qty8"))
        #DataStore.Add("DonatorRank", "VKIT2_QTY9", ini.GetSetting("VKIT_Level2", "Qty9"))
        #DataStore.Add("DonatorRank", "VKIT2_QTY10", ini.GetSetting("VKIT_Level2", "Qty10"))
        #DataStore.Add("DonatorRank", "DKIT1_INV1", ini.GetSetting("DKIT_Level1", "Inv1"))
        #DataStore.Add("DonatorRank", "DKIT1_INV2", ini.GetSetting("DKIT_Level1", "Inv2"))
        #DataStore.Add("DonatorRank", "DKIT1_INV3", ini.GetSetting("DKIT_Level1", "Inv3"))
        #DataStore.Add("DonatorRank", "DKIT1_INV4", ini.GetSetting("DKIT_Level1", "Inv4"))
        #DataStore.Add("DonatorRank", "DKIT1_INV5", ini.GetSetting("DKIT_Level1", "Inv5"))
        #DataStore.Add("DonatorRank", "DKIT1_INV6", ini.GetSetting("DKIT_Level1", "Inv6"))
        #DataStore.Add("DonatorRank", "DKIT1_INV7", ini.GetSetting("DKIT_Level1", "Inv7"))
        #DataStore.Add("DonatorRank", "DKIT1_INV8", ini.GetSetting("DKIT_Level1", "Inv8"))
        #DataStore.Add("DonatorRank", "DKIT1_INV9", ini.GetSetting("DKIT_Level1", "Inv9"))
        #DataStore.Add("DonatorRank", "DKIT1_INV10", ini.GetSetting("DKIT_Level1", "Inv10"))
        #DataStore.Add("DonatorRank", "DKIT1_QTY1", ini.GetSetting("DKIT_Level1", "Qty1"))
        #DataStore.Add("DonatorRank", "DKIT1_QTY2", ini.GetSetting("DKIT_Level1", "Qty2"))
        #DataStore.Add("DonatorRank", "DKIT1_QTY3", ini.GetSetting("DKIT_Level1", "Qty3"))
        #DataStore.Add("DonatorRank", "DKIT1_QTY4", ini.GetSetting("DKIT_Level1", "Qty4"))
        #DataStore.Add("DonatorRank", "DKIT1_QTY5", ini.GetSetting("DKIT_Level1", "Qty5"))
        #DataStore.Add("DonatorRank", "DKIT1_QTY6", ini.GetSetting("DKIT_Level1", "Qty6"))
        #DataStore.Add("DonatorRank", "DKIT1_QTY7", ini.GetSetting("DKIT_Level1", "Qty7"))
        #DataStore.Add("DonatorRank", "DKIT1_QTY8", ini.GetSetting("DKIT_Level1", "Qty8"))
        #DataStore.Add("DonatorRank", "DKIT1_QTY9", ini.GetSetting("DKIT_Level1", "Qty9"))
        #DataStore.Add("DonatorRank", "DKIT1_QTY10", ini.GetSetting("DKIT_Level1", "Qty10"))
        #DataStore.Add("DonatorRank", "DKIT2_INV1", ini.GetSetting("DKIT_Level2", "Inv1"))
        #DataStore.Add("DonatorRank", "DKIT2_INV2", ini.GetSetting("DKIT_Level2", "Inv2"))
        #DataStore.Add("DonatorRank", "DKIT2_INV3", ini.GetSetting("DKIT_Level2", "Inv3"))
        #DataStore.Add("DonatorRank", "DKIT2_INV4", ini.GetSetting("DKIT_Level2", "Inv4"))
        #DataStore.Add("DonatorRank", "DKIT2_INV5", ini.GetSetting("DKIT_Level2", "Inv5"))
        #DataStore.Add("DonatorRank", "DKIT2_INV6", ini.GetSetting("DKIT_Level2", "Inv6"))
        #DataStore.Add("DonatorRank", "DKIT2_INV7", ini.GetSetting("DKIT_Level2", "Inv7"))
        #DataStore.Add("DonatorRank", "DKIT2_INV8", ini.GetSetting("DKIT_Level2", "Inv8"))
        #DataStore.Add("DonatorRank", "DKIT2_INV9", ini.GetSetting("DKIT_Level2", "Inv9"))
        #DataStore.Add("DonatorRank", "DKIT2_INV10", ini.GetSetting("DKIT_Level2", "Inv10"))
        #DataStore.Add("DonatorRank", "DKIT2_QTY1", ini.GetSetting("DKIT_Level2", "Qty1"))
        #DataStore.Add("DonatorRank", "DKIT2_QTY2", ini.GetSetting("DKIT_Level2", "Qty2"))
        #DataStore.Add("DonatorRank", "DKIT2_QTY3", ini.GetSetting("DKIT_Level2", "Qty3"))
        #DataStore.Add("DonatorRank", "DKIT2_QTY4", ini.GetSetting("DKIT_Level2", "Qty4"))
        #DataStore.Add("DonatorRank", "DKIT2_QTY5", ini.GetSetting("DKIT_Level2", "Qty5"))
        #DataStore.Add("DonatorRank", "DKIT2_QTY6", ini.GetSetting("DKIT_Level2", "Qty6"))
        #DataStore.Add("DonatorRank", "DKIT2_QTY7", ini.GetSetting("DKIT_Level2", "Qty7"))
        #DataStore.Add("DonatorRank", "DKIT2_QTY8", ini.GetSetting("DKIT_Level2", "Qty8"))
        #DataStore.Add("DonatorRank", "DKIT2_QTY9", ini.GetSetting("DKIT_Level2", "Qty9"))
        #DataStore.Add("DonatorRank", "DKIT2_QTY10", ini.GetSetting("DKIT_Level2", "Qty10"))
        DataStore.Add("DonatorRank", "JoinMSG", ini.GetSetting("Settings", "JoinMessages"))
        DataStore.Add("DonatorRank", "LeaveMSG", ini.GetSetting("Settings", "LeaveMessages"))
        DataStore.Add("DonatorRank", "ChatPrefix", ini.GetSetting("Settings", "ChatPrefix"))
        DataStore.Add("DonatorRank", "OwnerID", ini.GetSetting("Settings", "OwnerSteamID"))
        DataStore.Add("DonatorRank", "OwnerColour", ini.GetSetting("Settings", "OwnerColour"))
        DataStore.Add("DonatorRank", "AdminColour", ini.GetSetting("Settings", "AdminColour"))
        DataStore.Add("DonatorRank", "ModColour", ini.GetSetting("ModSettings", "ModeratorColour"))
        DataStore.Add("DonatorRank", "DonatorColour", ini.GetSetting("DonatorSettings", "DonatorColour"))
        DataStore.Add("DonatorRank", "VIPColour", ini.GetSetting("VIPSettings", "VIPColour"))
        DataStore.Add("DonatorRank", "LogTPS", ini.GetSetting("Settings", "LogTps"))
        DataStore.Add("DonatorRank", "LogKicks", ini.GetSetting("Settings", "LogKicks"))
        DataStore.Add("DonatorRank", "LogBroadcasts", ini.GetSetting("Settings", "LogBroadcast"))
        DataStore.Add("DonatorRank", "PlayerHomesMax", ini.GetSetting("Settings", "PlayerMaxhomes"))
        DataStore.Add("DonatorRank", "ModHomesMax", ini.GetSetting("ModSettings", "Maxhomes"))
        DataStore.Add("DonatorRank", "DonatorHomesMax", ini.GetSetting("DonatorSettings", "Maxhomes"))
        DataStore.Add("DonatorRank", "VIPHomesMax", ini.GetSetting("VIPSettings", "Maxhomes"))
        DataStore.Add("DonatorRank", "DTPCoolDown", ini.GetSetting("DonatorSettings", "TPCooldown"))
        DataStore.Add("DonatorRank", "VTPCoolDown", ini.GetSetting("VIPSettings", "TPCooldown"))
        DataStore.Add("DonatorRank", "LVL1DKITCoolDown", ini.GetSetting("DonatorSettings", "LVL1KitCooldown"))
        DataStore.Add("DonatorRank", "LVL1VKITCoolDown", ini.GetSetting("VIPSettings", "LVL1KitCooldown"))
        DataStore.Add("DonatorRank", "LVL2DKITCoolDown", ini.GetSetting("DonatorSettings", "LVL2KitCooldown"))
        DataStore.Add("DonatorRank", "LVL2VKITCoolDown", ini.GetSetting("VIPSettings", "LVL2KitCooldown"))
 
    def On_Command(self, Player, cmd, args):
        if cmd == "donatorhelp":
            if len(args) == 0:
                users = self.getUserIni()
                rank = users.GetSetting(Player.SteamID, "Rank")
                if Player.Admin or rank == "VIP" or rank == "Donator" or rank == "Moderator":
                    if users.GetSetting(Player.SteamID, "AddVIPS") == "true" or Player.Admin:
                        Player.Message("/vadd [playername] - Add player as Vip")
                    if users.GetSetting(Player.SteamID, "AddDonators") == "true" or Player.Admin:
                        Player.Message("/dadd [playername] - Add player as Donator")
                    if users.GetSetting(Player.SteamID, "AddMods") == "true" or Player.Admin:
                        Player.Message("/madd [playername] - Add player as Mod")
                    if users.GetSetting(Player.SteamID, "DelVIPS") == "true" or Player.Admin:
                        Player.Message("/vdel [playername] - Remove player as Vip")
                    if users.GetSetting(Player.SteamID, "DelDonators") == "true" or Player.Admin:
                        Player.Message("/ddel [playername] - Remove player as Donator")
                    if users.GetSetting(Player.SteamID, "DelMods") == "true" or Player.Admin:
                        Player.Message("/mdel [playername] - Remove player as Mod")
                    if users.GetSetting(Player.SteamID, "LVL1VKIT") == "true" or Player.Admin:
                        Player.Message("/vkit basic - Get the basic VIP kit")
                    if users.GetSetting(Player.SteamID, "LVL2VKIT") == "true" or Player.Admin:
                        Player.Message("/vkit advanced - Get the basic VIP kit")
                    if users.GetSetting(Player.SteamID, "LVL1DKIT") == "true" or Player.Admin:
                        Player.Message("/dkit basic - Get the basic Donator kit")
                    if users.GetSetting(Player.SteamID, "LVL2DKIT") == "true" or Player.Admin:
                        Player.Message("/dkit advanced - Get the basic Donator kit")
                    if users.GetSetting(Player.SteamID, "MODKIT") == "true" or Player.Admin:
                        Player.Message("/mkit - Gives you invisible suit + uber items")
                    if users.GetSetting(Player.SteamID, "CanKick") == "true" or Player.Admin:
                        Player.Message("/mkick [Name] - Kicks a player")
                    if users.GetSetting(Player.SteamID, "CanBan") == "true" or Player.Admin:
                        Player.Message("/mban - Shoot a player to ban them")
                        Player.Message("/mban [Name] - To ban a player by their name instead of shooting")
                        Player.Message("/cban - To cancel shooting a player to ban")
                    if users.GetSetting(Player.SteamID, "VTP") == "true" or Player.Admin:
                        Player.Message("/vtp - Teleport to preset locations")
                    if users.GetSetting(Player.SteamID, "DTP") == "true" or Player.Admin:
                        Player.Message("/dtp - Teleport to preset locations")
                    if users.GetSetting(Player.SteamID, "MTP") == "true" or Player.Admin:
                        Player.Message("/mtp [Name] - Teleport to a player")
                        Player.Message("/mtpback - Teleport back to where you were")
                    if users.GetSetting(Player.SteamID, "UseBroadcast") == "true" or Player.Admin:
                        Player.Message("/yell - Tell the server something")
                    if users.GetSetting(Player.SteamID, "AccessInfo") == "true" or Player.Admin:
                        Player.Message("/info [Name] - Get info about a player")
                else:
                    Player.MessageFrom("DonatorRank", "Contact a staff member about becoming a VIP/Donator/Moderator")
            else:
                Player.Message("Usage: /donatorhelp")
 
        elif cmd == "yell":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "UseBroadcast") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /yell [Message]")
                elif args.Length > 0:
                    text = self.argsToText(args)
                    Server.BroadcastFrom("Player Broadcast", text)
                    if DataStore.Get("DonatorRank", "LogBroadcasts") == "true":
                        ini = self.getLogIni()
                        date = Plugin.GetDate()
                        time = Plugin.GetTime()
                        ini.AddSetting("BoardCasterLog", date + "|" + time + " || " + Player.Name, Player.SteamID + " said: [" + text + "]")
                        ini.Save()
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "vadd":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "AddVIPS") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /vadd [playername]")
                elif len(args) > 0:
                    vipname = self.CheckV(Player, args)
                    if vipname is not None:
                        if self.isDonator(vipname):
                            Player.Message(vipname.Name + " is a Donator, use /ddel " + vipname.Name)
                        elif self.isMod(vipname):
                            Player.Message(vipname.Name + " is a Moderator, use /mdel " + vipname.Name)
                        elif not self.isVIP(vipname):
                            d = Plugin.GetDate()
                            t = Plugin.GetTime()
                            p = Player.Name
                            users.AddSetting(vipname.SteamID, "UserName", vipname.Name)
                            users.AddSetting(vipname.SteamID, "INFO", "Time: " + t + "||Date: " + d + "||By: " + p)
                            users.AddSetting(vipname.SteamID, "Rank", "VIP")
                            users.AddSetting(vipname.SteamID, "MaxHomes", DataStore.Get("DonatorRank", "VIPHomesMax"))
                            users.AddSetting(vipname.SteamID, "AddVIPS", "false")
                            users.AddSetting(vipname.SteamID, "AddDonators", "false")
                            users.AddSetting(vipname.SteamID, "AddMods", "false")
                            users.AddSetting(vipname.SteamID, "DelVIPS", "false")
                            users.AddSetting(vipname.SteamID, "DelDonators", "false")
                            users.AddSetting(vipname.SteamID, "DelMods", "false")
                            users.AddSetting(vipname.SteamID, "LVL1VKIT", "true")
                            users.AddSetting(vipname.SteamID, "LVL2VKIT", "false")
                            users.AddSetting(vipname.SteamID, "LVL1DKIT", "false")
                            users.AddSetting(vipname.SteamID, "LVL2DKIT", "false")
                            users.AddSetting(vipname.SteamID, "MODKIT", "false")
                            users.AddSetting(vipname.SteamID, "CanKick", "false")
                            users.AddSetting(vipname.SteamID, "CanBan", "false")
                            users.AddSetting(vipname.SteamID, "VTP", "true")
                            users.AddSetting(vipname.SteamID, "DTP", "false")
                            users.AddSetting(vipname.SteamID, "MTP", "false")
                            users.AddSetting(vipname.SteamID, "UseBroadcast", "true")
                            users.AddSetting(vipname.SteamID, "AccessInfo", "false")
                            users.Save()
                            Server.Broadcast("[color#FFFF00]" + vipname.Name + " [color#FFFFFF]is now a VIP!")
                            vipname.Message("Use /donatorhelp to show the command list available for you.")
                        else:
                            Player.Message(vipname.Name + " is already a VIP.")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "dadd":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "AddDonators") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /dadd [playername]")
                elif len(args) > 0:
                    donname = self.CheckV(Player, args)
                    if donname is not None:
                        if self.isVIP(donname):
                            Player.Message(donname.Name + " is a VIP, use /vdel " + donname.Name)
                        elif self.isMod(donname):
                            Player.Message(donname.Name + " is a Moderator, use /mdel " + donname.Name)
                        elif not self.isDonator(donname):
                            d = Plugin.GetDate()
                            t = Plugin.GetTime()
                            p = Player.Name
                            ds = DataStore
                            users.AddSetting(donname.SteamID, "UserName", donname.Name)
                            users.AddSetting(donname.SteamID, "INFO", "Time: " + t + "||Date: " + d + "||By: " + p)
                            users.AddSetting(donname.SteamID, "Rank", "Donator")
                            users.AddSetting(donname.SteamID, "MaxHomes", ds.Get("DonatorRank", "DonatorHomesMax"))
                            users.AddSetting(donname.SteamID, "AddVIPS", "false")
                            users.AddSetting(donname.SteamID, "AddDonators", "false")
                            users.AddSetting(donname.SteamID, "AddMods", "false")
                            users.AddSetting(donname.SteamID, "DelVIPS", "false")
                            users.AddSetting(donname.SteamID, "DelDonators", "false")
                            users.AddSetting(donname.SteamID, "DelMods", "false")
                            users.AddSetting(donname.SteamID, "LVL1VKIT", "false")
                            users.AddSetting(donname.SteamID, "LVL2VKIT", "false")
                            users.AddSetting(donname.SteamID, "LVL1DKIT", "true")
                            users.AddSetting(donname.SteamID, "LVL2DKIT", "false")
                            users.AddSetting(donname.SteamID, "MODKIT", "false")
                            users.AddSetting(donname.SteamID, "CanKick", "false")
                            users.AddSetting(donname.SteamID, "CanBan", "false")
                            users.AddSetting(donname.SteamID, "VTP", "false")
                            users.AddSetting(donname.SteamID, "DTP", "true")
                            users.AddSetting(donname.SteamID, "MTP", "false")
                            users.AddSetting(donname.SteamID, "UseBroadcast", "true")
                            users.AddSetting(donname.SteamID, "AccessInfo", "false")
                            users.Save()
                            Server.Broadcast("[color#FFFF00]" + donname.Name + " [color#FFFFFF]is now a Donator!")
                            donname.Message("Use /donatorhelp to show the command list available for you.")
                        else:
                            Player.Message(donname.Name + " is already a Donator")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "madd":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "AddMods") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /madd [playername]")
                elif len(args) > 0:
                    modname = self.CheckV(Player, args)
                    if modname is not None:
                        if self.isVIP(modname):
                            Player.Message(modname.Name + " is a VIP, use /vdel " + modname.Name)
                        elif self.isDonator(modname):
                            Player.Message(modname.Name + " is a Donator, use /ddel " + modname.Name)
                        elif not self.isMod(modname):
                            d = Plugin.GetDate()
                            t = Plugin.GetTime()
                            p = Player.Name
                            users.AddSetting(modname.SteamID, "UserName", modname.Name)
                            users.AddSetting(modname.SteamID, "INFO", "Time: " + t + "||Date: " + d + "||By: " + p)
                            users.AddSetting(modname.SteamID, "Rank", "Mod")
                            users.AddSetting(modname.SteamID, "MaxHomes", DataStore.Get("DonatorRank", "ModHomesMax"))
                            users.AddSetting(modname.SteamID, "AddVIPS", "true")
                            users.AddSetting(modname.SteamID, "AddDonators", "true")
                            users.AddSetting(modname.SteamID, "AddMods", "false")
                            users.AddSetting(modname.SteamID, "DelVIPS", "true")
                            users.AddSetting(modname.SteamID, "DelDonators", "true")
                            users.AddSetting(modname.SteamID, "DelMods", "false")
                            users.AddSetting(modname.SteamID, "LVL1VKIT", "false")
                            users.AddSetting(modname.SteamID, "LVL2VKIT", "false")
                            users.AddSetting(modname.SteamID, "LVL1DKIT", "false")
                            users.AddSetting(modname.SteamID, "LVL2DKIT", "false")
                            users.AddSetting(modname.SteamID, "MODKIT", "true")
                            users.AddSetting(modname.SteamID, "CanKick", "true")
                            users.AddSetting(modname.SteamID, "CanBan", "true")
                            users.AddSetting(modname.SteamID, "VTP", "false")
                            users.AddSetting(modname.SteamID, "DTP", "false")
                            users.AddSetting(modname.SteamID, "MTP", "true")
                            users.AddSetting(modname.SteamID, "UseBroadcast", "true")
                            users.AddSetting(modname.SteamID, "AccessInfo", "true")
                            users.Save()
                            Server.Broadcast("[color#FFFF00]" + modname.Name + " [color#FFFFFF]is now a Moderator!")
                            modname.Message("Use /donatorhelp to show the command list available for you.")
                        else:
                            Player.Message(modname.Name + " is already a Moderator")
            else:
                Player.Message("You don't have permission to use this command!")

        elif cmd == "addmoderator":
            if self.isMod(Player):
                if len(args) > 0:
                    name = self.CheckV(Player, args)
                    self.isMod(name)
            return
 
        elif cmd == "vdel":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "DelVIPS") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /vdel [playername]")
                elif len(args) > 0:
                    vipname = self.CheckV(Player, args)
                    if vipname is not None:
                        if self.isDonator(vipname):
                            Player.Message(vipname.Name + " is a Donator, use /ddel " + vipname.Name)
                        elif self.isMod(vipname):
                            Player.Message(vipname.Name + " is a Moderator, use /mdel " + vipname.Name)
                        else:
                            users.DeleteSetting(vipname.SteamID, "UserName")
                            users.DeleteSetting(vipname.SteamID, "INFO")
                            users.DeleteSetting(vipname.SteamID, "Rank")
                            users.DeleteSetting(vipname.SteamID, "MaxHomes")
                            users.DeleteSetting(vipname.SteamID, "AddVIPS")
                            users.DeleteSetting(vipname.SteamID, "AddDonators")
                            users.DeleteSetting(vipname.SteamID, "AddMods")
                            users.DeleteSetting(vipname.SteamID, "DelVIPS")
                            users.DeleteSetting(vipname.SteamID, "DelDonators")
                            users.DeleteSetting(vipname.SteamID, "DelMods")
                            users.DeleteSetting(vipname.SteamID, "LVL1VKIT")
                            users.DeleteSetting(vipname.SteamID, "LVL2VKIT")
                            users.DeleteSetting(vipname.SteamID, "LVL1DKIT")
                            users.DeleteSetting(vipname.SteamID, "LVL2DKIT")
                            users.DeleteSetting(vipname.SteamID, "MODKIT")
                            users.DeleteSetting(vipname.SteamID, "CanKick")
                            users.DeleteSetting(vipname.SteamID, "CanBan")
                            users.DeleteSetting(vipname.SteamID, "VTP")
                            users.DeleteSetting(vipname.SteamID, "DTP")
                            users.DeleteSetting(vipname.SteamID, "MTP")
                            users.DeleteSetting(vipname.SteamID, "UseBroadcast")
                            users.DeleteSetting(vipname.SteamID, "AccessInfo")
                            users.Save()
                            Player.Message(vipname.Name + " is no longer a VIP")
                            vipname.Message("You are not longer a VIP")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "ddel":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "DelDonators") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /ddel [playername]")
                elif len(args) > 0:
                    donname = self.CheckV(Player, args)
                    if donname is not None:
                        if self.isVIP(donname):
                            Player.Message(donname.Name + " is a VIP, use /vdel " + donname.Name)
                        elif self.isMod(donname):
                            Player.Message(donname.Name + " is a Moderator, use /mdel " + donname.Name)
                        else:
                            users.DeleteSetting(donname.SteamID, "UserName")
                            users.DeleteSetting(donname.SteamID, "INFO")
                            users.DeleteSetting(donname.SteamID, "Rank")
                            users.DeleteSetting(donname.SteamID, "MaxHomes")
                            users.DeleteSetting(donname.SteamID, "AddVIPS")
                            users.DeleteSetting(donname.SteamID, "AddDonators")
                            users.DeleteSetting(donname.SteamID, "AddMods")
                            users.DeleteSetting(donname.SteamID, "DelVIPS")
                            users.DeleteSetting(donname.SteamID, "DelDonators")
                            users.DeleteSetting(donname.SteamID, "DelMods")
                            users.DeleteSetting(donname.SteamID, "LVL1VKIT")
                            users.DeleteSetting(donname.SteamID, "LVL2VKIT")
                            users.DeleteSetting(donname.SteamID, "LVL1DKIT")
                            users.DeleteSetting(donname.SteamID, "LVL2DKIT")
                            users.DeleteSetting(donname.SteamID, "MODKIT")
                            users.DeleteSetting(donname.SteamID, "CanKick")
                            users.DeleteSetting(donname.SteamID, "CanBan")
                            users.DeleteSetting(donname.SteamID, "VTP")
                            users.DeleteSetting(donname.SteamID, "DTP")
                            users.DeleteSetting(donname.SteamID, "MTP")
                            users.DeleteSetting(donname.SteamID, "UseBroadcast")
                            users.DeleteSetting(donname.SteamID, "AccessInfo")
                            users.Save()
                            Player.Message(donname.Name + " is no longer a Donator")
                            donname.Message("you are no longer a Donator")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "mdel":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "DelMods") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /mdel [playername]")
                elif len(args) > 0:
                    modname = self.CheckV(Player, args)
                    if modname is not None:
                        if self.isVIP(modname):
                            Player.Message(modname.Name + " is a VIP, use /vdel " + modname.Name)
                        elif self.isDonator(modname):
                            Player.Message(modname.Name + " is a Donator, use /ddel " + modname.Name)
                        else:
                            users.DeleteSetting(modname.SteamID, "UserName")
                            users.DeleteSetting(modname.SteamID, "INFO")
                            users.DeleteSetting(modname.SteamID, "Rank")
                            users.DeleteSetting(modname.SteamID, "MaxHomes")
                            users.DeleteSetting(modname.SteamID, "AddVIPS")
                            users.DeleteSetting(modname.SteamID, "AddDonators")
                            users.DeleteSetting(modname.SteamID, "AddMods")
                            users.DeleteSetting(modname.SteamID, "DelVIPS")
                            users.DeleteSetting(modname.SteamID, "DelDonators")
                            users.DeleteSetting(modname.SteamID, "DelMods")
                            users.DeleteSetting(modname.SteamID, "LVL1VKIT")
                            users.DeleteSetting(modname.SteamID, "LVL2VKIT")
                            users.DeleteSetting(modname.SteamID, "LVL1DKIT")
                            users.DeleteSetting(modname.SteamID, "LVL2DKIT")
                            users.DeleteSetting(modname.SteamID, "MODKIT")
                            users.DeleteSetting(modname.SteamID, "CanKick")
                            users.DeleteSetting(modname.SteamID, "CanBan")
                            users.DeleteSetting(modname.SteamID, "VTP")
                            users.DeleteSetting(modname.SteamID, "DTP")
                            users.DeleteSetting(modname.SteamID, "MTP")
                            users.DeleteSetting(modname.SteamID, "UseBroadcast")
                            users.DeleteSetting(modname.SteamID, "AccessInfo")
                            users.Save()
                            Player.Message(modname.Name + " is no longer a Moderator")
                            modname.Message("You are no longer a Moderator")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "vkit":
            if len(args) == 0:
                Player.Message("Usage: /vkit [basic / advanced]")
            elif len(args) == 1:
                if args[0] == "basic":
                    users = self.getUserIni()
                    if users.GetSetting(Player.SteamID, "LVL1VKIT") == "true" or Player.Admin:
                        if Player.Inventory.FreeSlots < 10:
                            Player.Message("You need atleast 10 free spaces!")
                        else:
                            sett = self.GetSettingsIni()
                            waittime = int(sett.GetSetting("VIPSettings", "LVL1KitCooldown"))
                            if DataStore.Get("LVL1VKitCooldown", Player.SteamID) is None:
                                time = 0
                            else:
                                time = DataStore.Get("LVL2DKitCooldown", Player.SteamID)
                                time = int(time)
                            calc = System.Environment.TickCount - time
                            if calc >= waittime or Player.Admin:
                                DataStore.Add("LVL1VKitCooldown", Player.SteamID, System.Environment.TickCount)
                                Player.Notice("Here are your items!")
                                self.vkit1(sett, Player)
                            else:
                                workingout = (round(waittime / 1000, 2) / 60) - round(int(calc) / 1000, 2) / 60
                                current = round(workingout, 2)
                                Player.Message(str(current) + " Minutes remaining before you can use this.")
                    else:
                        Player.Message("You don't have permission to use this command!")
                elif args[0] == "advanced":
                    users = self.getUserIni()
                    if users.GetSetting(Player.SteamID, "LVL2VKIT") == "true" or Player.Admin:
                        if Player.Inventory.FreeSlots < 10:
                            Player.Message("You need atleast 10 free spaces!")
                        else:
                            sett = self.GetSettingsIni()
                            waittime = int(sett.GetSetting("VIPSettings", "LVL2KitCooldown"))
                            if DataStore.Get("LVL2VKitCooldown", Player.SteamID) is None:
                                time = 0
                            else:
                                time = DataStore.Get("LVL2DKitCooldown", Player.SteamID)
                                time = int(time)
                            calc = System.Environment.TickCount - time
                            if calc >= waittime or Player.Admin or time == 0:
                                DataStore.Add("LVL2VKitCooldown", Player.SteamID, System.Environment.TickCount)
                                Player.Notice("Here are your items!")
                                self.vkit2(sett, Player)
                            else:
                                workingout = (round(waittime / 1000, 2) / 60) - round(int(calc) / 1000, 2) / 60
                                current = round(workingout, 2)
                                Player.Message(str(current) + " Minutes remaining before you can use this.")
                    else:
                        Player.Message("You don't have permission to use this command!")
 
        elif cmd == "dkit":
            if len(args) == 0:
                Player.Message("Usage: /dkit [basic / advanced]")
            elif len(args) == 1:
                if args[0] == "basic":
                    users = self.getUserIni()
                    if users.GetSetting(Player.SteamID, "LVL1DKIT") == "true" or Player.Admin:
                        if Player.Inventory.FreeSlots < 10:
                            Player.Message("You need atleast 10 free spaces!")
                        else:
                            sett = self.GetSettingsIni()
                            waittime = int(sett.GetSetting("DonatorSettings", "LVL1KitCooldown"))
                            if DataStore.Get("LVL1DKitCooldown", Player.SteamID) is None:
                                time = 0
                            else:
                                time = DataStore.Get("LVL2DKitCooldown", Player.SteamID)
                                time = int(time)
                            calc = System.Environment.TickCount - int(time)
                            if calc >= waittime or Player.Admin or time == 0:
                                DataStore.Add("LVL1DKitCooldown", Player.SteamID, System.Environment.TickCount)
                                Player.Notice("Here are your items!")
                                self.dkit1(sett, Player)
                            else:
                                workingout = (round(waittime / 1000, 2) / 60) - round(int(calc) / 1000, 2) / 60
                                current = round(workingout, 2)
                                Player.Message(str(current) + " Minutes remaining before you can use this.")
                    else:
                        Player.Message("You don't have permission to use this command!")
                elif args[0] == "advanced":
                    users = self.getUserIni()
                    if users.GetSetting(Player.SteamID, "LVL2DKIT") == "true" or Player.Admin:
                        if Player.Inventory.FreeSlots < 10:
                            Player.Message("You need atleast 10 free spaces!")
                        else:
                            sett = self.GetSettingsIni()
                            waittime = int(sett.GetSetting("DonatorSettings", "LVL2KitCooldown"))
                            if DataStore.Get("LVL2DKitCooldown", Player.SteamID) is None:
                                time = 0
                            else:
                                time = DataStore.Get("LVL2DKitCooldown", Player.SteamID)
                                time = int(time)
                            calc = System.Environment.TickCount - time
                            if calc >= waittime or Player.Admin or time == 0:
                                DataStore.Add("LVL2DKitCooldown", Player.SteamID, System.Environment.TickCount)
                                Player.Notice("Here are your items!")
                                self.dkit2(sett, Player)
                            else:
                                workingout = (round(waittime / 1000, 2) / 60) - round(int(calc) / 1000, 2) / 60
                                current = round(workingout, 2)
                                Player.Message(str(current) + " Minutes remaining before you can use this.")
                    else:
                        Player.Message("You don't have permission to use this command!")
 
        elif cmd == "mkit":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "MODKIT") == "true" or Player.Admin:
                if len(args) == 0:
                    if Player.Inventory.FreeSlots < 4:
                        Player.Message("You need atleast 4 spots free!")
                    else:
                        Player.Inventory.RemoveItem(36)
                        Player.Inventory.RemoveItem(37)
                        Player.Inventory.RemoveItem(38)
                        Player.Inventory.RemoveItem(39)
                        Player.Inventory.AddItemTo("Invisible Helmet", 36, 1)
                        Player.Inventory.AddItemTo("Invisible Vest", 37, 1)
                        Player.Inventory.AddItemTo("Invisible Pants", 38, 1)
                        Player.Inventory.AddItemTo("Invisible Boots", 39, 1)
                        Player.Inventory.AddItem("Uber Hatchet", 1)
                        Player.Inventory.AddItem("Uber Hunting Bow", 1)
                        Player.Inventory.AddItem("Arrow", 20)
                        Player.Inventory.AddItem("Small Rations", 5)
                        Player.Message("You are now invisible!")
                else:
                    Player.Message("Usage: /mkit")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "vtp":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "VTP") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("Teleport locations:")
                    Player.Message("Smallrad, Bigrad")
                    Player.Message("Factory, Hangar")
                elif len(args) == 1:
                    waittime = int(DataStore.Get("DonatorRank", "VTPCoolDown"))
                    time = DataStore.Get("VTPCooldown", Player.SteamID)
                    time = int(time)
                    if time is None:
                        time = 0
                    elif args[0] == "Smallrad":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(6050, 381, -3620)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("Small Rad Town")
                            Player.SafeTeleportTo(6050, 381, -3620)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    elif args[0] == "Bigrad":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(5250, 371, -4850)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("Big Rad Town")
                            Player.SafeTeleportTo(5250, 371, -4850)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    elif args[0] == "Factory":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(6300, 361, -4650)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("Factory Rad")
                            Player.SafeTeleportTo(6300, 361, -4650)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    elif args[0] == "Hangar":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(6600, 356, -4400)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("Hangar")
                            Player.SafeTeleportTo(6600, 356, -4400)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    else:
                        Player.Message("Usage: /vtp [Location]")
                else:
                    Player.Message("Usage: /vtp [Location]")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "dtp":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "DTP") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("Teleport locations:")
                    Player.Message("Smallrad, Bigrad")
                    Player.Message("Factory, Hangar")
                    Player.Message("Tankers, Hackervalley")
                    Player.Message("French, Nextvalley")
                elif len(args) == 1:
                    waittime = int(DataStore.Get("DonatorRank", "DTPCoolDown"))
                    time = DataStore.Get("DTPCooldown", Player.SteamID)
                    time = int(time)
                    if time is None:
                        time = 0
                    elif args[0] == "Smallrad":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(6050, 381, -3620)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("Small Rad Town")
                            Player.SafeTeleportTo(6050, 381, -3620)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    elif args[0] == "Bigrad":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(5250, 371, -4850)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("Big Rad Town")
                            Player.SafeTeleportTo(5250, 371, -4850)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    elif args[0] == "Factory":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(6600, 356, -4400)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("Factory Rad")
                            Player.SafeTeleportTo(6600, 356, -4400)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    elif args[0] == "Hangar":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(6600, 356, -4400)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("Hangar")
                            Player.SafeTeleportTo(6600, 356, -4400)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    elif args[0] == "Tankers":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(6690, 356, -3880)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("Oil Tankers")
                            Player.SafeTeleportTo(6690, 356, -3880)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    elif args[0] == "Hackervalley":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(5000, 461, -3000)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("North Hacker Valley")
                            Player.SafeTeleportTo(5000, 461, -3000)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    elif args[0] == "French":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(6056, 385, -4162)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("French Valley")
                            Player.SafeTeleportTo(6056, 385, -4162)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    elif args[0] == "Nextvalley":
                        calc = System.Environment.TickCount - time
                        if calc >= waittime or Player.Admin:
                            Player.SafeTeleportTo(4668, 445, -3908)
                            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
                            Player.InventoryNotice("Next Valley")
                            Player.SafeTeleportTo(4668, 445, -3908)
                        else:
                            Player.Notice("You have to wait before teleporting again!")
                    else:
                        Player.Message("Usage: /dtp [Location]")
                else:
                    Player.Message("Usage: /dtp [Location]")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "mtp":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "MTP") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /mtp [Player Name]")
                if len(args) > 0:
                    targetname = self.CheckV(Player, args)
                    if targetname is None:
                        return
                    plocation = Player.Location
                    DataStore.Add("MODLOCATION", Player.SteamID, plocation)
                    targetname.Notice(Player.Name + " has teleported to you!")
                    Player.TeleportTo(targetname)
                    Player.Message("Teleported to: " + targetname.Name)
                    Player.Message("To teleport back to where you were, Type /mtpback")
                    Player.TeleportTo(targetname)
                    if DataStore.Get("DonatorRank", "LogTPS") == "true":
                        ini = self.getLogIni()
                        date = Plugin.GetDate()
                        tym = Plugin.GetTime()
                        ini.AddSetting("TPLog", date + "| " + tym + " || " + Player.Name + " Teleported to: " + targetname.Name, targetname.SteamID)
                        ini.Save()
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "mtpback":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "MTP") == "true" or Player.Admin:
                if DataStore.Get("MODLOCATION", Player.SteamID):
                    plocation = DataStore.Get("MODLOCATION", Player.SteamID)
                    Player.SafeTeleportTo(plocation)
                    Player.Message("You have been teleported back")
                    DataStore.Remove("MODLOCATION", Player.SteamID)
                    Player.SafeTeleportTo(plocation)
                else:
                    Player.Message("You have no last locations")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "mban":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "CanBan") == "true" or Player.Admin:
                if len(args) == 0:
                    DataStore.Add("ModBan", Player.SteamID, "on")
                    Player.Message("Shoot the player to ban them")
                    Player.Message("Or you can type /mban [username]")
                    Player.Message("Type /cban to cancel this action")
                elif len(args) > 0:
                    targetname = self.CheckV(Player, args)
                    if targetname is not None:
                        ini = self.BansListIni()
                        ini.AddSetting("BannedIPs", targetname.IP, targetname.Name + " was banned by: " + Player.Name)
                        ini.AddSetting("BannedIDs", targetname.SteamID, targetname.Name + " was banned by: " + Player.Name)
                        ini.Save()
                        Server.Broadcast("[color red]" + targetname.Name + "[/color] has been banned by: [color red]" + Player.Name)
                        if DataStore.Get("ModBan", Player.SteamID) == "on":
                            DataStore.Remove("ModBan", Player.SteamID)
                            Player.Message("You can now safely shoot another player")
                        targetname.Disconnect()
                    else:
                        return
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "cban":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "CanBan") == "true" or Player.Admin:
                if DataStore.Get("ModBan", Player.SteamID) == "on":
                    DataStore.Remove("ModBan", Player.SteamID)
                    Player.Message("You can now shoot a player safely")
                else:
                    Player.Message("You never had this command enabled")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "mkick":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "CanKick") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("usage: /mkick [name]")
                elif len(args) > 0:
                    targetname = self.CheckV(Player, args)
                    if targetname is not None:
                        pn = targetname.Name
                        targetname.Message("You have been kicked by: " + Player.Name)
                        Server.Broadcast("[color red]" + pn + " [/color]has been kicked by: [color red]" + Player.Name)
                        if DataStore.Get("DonatorRank", "LogKicks") == "true":
                            ini = self.getLogIni()
                            date = Plugin.GetDate()
                            tym = Plugin.GetTime()
                            pyid = targetname.SteamID
                            tname = targetname.Name
                            ini.AddSetting("KickedList", date + "| " + tym + " || " + Player.Name + " kicked: " + tname, pyid)
                            ini.Save()
                        targetname.Disconnect()
                    else:
                        return
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "info":
            users = self.getUserIni()
            if users.GetSetting(Player.SteamID, "AccessInfo") == "true" or Player.Admin:
                if len(args) == 0:
                    Player.Message("usage: /info [name]")
                elif len(args) > 0:
                    targetname = self.CheckV(Player, args)
                    if targetname is None:
                        return
                    else:
                        pip = targetname.IP
                        plocation = str(targetname.Location)
                        pping = str(targetname.Ping)
                        pid = targetname.SteamID
                        pn = targetname.Name
                        Player.Message("Info about " + pn)
                        Player.Message("IP: [color cyan]" + pip)
                        Player.Message("SteamID: [color cyan]" + pid)
                        Player.Message("Current Location: [color cyan]" + plocation)
                        Player.Message("Ping: [color cyan]" + pping)
            else:
                Player.Message("You don't have permission to use this command!")
 
    def On_PlayerConnected(self, Player):
        try:
            ini = self.getUserIni()
            if ini.GetSetting(Player.SteamID, "MaxHomes") is not None:
                DataStore.Add("MaxHomes", Player.SteamID, int(ini.GetSetting(Player.SteamID, "MaxHomes")))
            DataStore.Add("MTPCooldown", Player.SteamID, System.Environment.TickCount)
            DataStore.Add("VTPCooldown", Player.SteamID, System.Environment.TickCount)
            DataStore.Add("DTPCooldown", Player.SteamID, System.Environment.TickCount)
            DataStore.Add("LVL1DKitCooldown", Player.SteamID, System.Environment.TickCount)
            DataStore.Add("LVL2DKitCooldown", Player.SteamID, System.Environment.TickCount)
            DataStore.Add("LVL1VKitCooldown", Player.SteamID, System.Environment.TickCount)
            DataStore.Add("LVL2VKitCooldown", Player.SteamID, System.Environment.TickCount)
            if self.isBanned(Player):
                Player.Notice("Talk to the server owner about getting unbanned!")
                Server.Broadcast("A user with the banned IP: [[color cyan]" + Player.IP + "[/color]] is trying to connect!")
                Player.Disconnect()
            elif DataStore.Get("DonatorRank", "JoinMMSG") == "true":
                if self.isBanned(Player):
                    return
                elif Player.SteamID == DataStore.Get("DonatorRank", "OwnerID"):
                    Server.BroadcastFrom("Owner", Player.Name + " is now Online.")
                elif Player.Admin:
                    Server.BroadcastFrom("Admin", Player.Name + " is now Online.")
                elif self.isMod(Player):
                    Server.BroadcastFrom("Moderator", Player.Name + " is now Online.")
                elif self.isDonator(Player):
                    Server.BroadcastFrom("Donator", Player.Name + " is now Online.")
                elif self.isVIP(Player):
                    Server.BroadcastFrom("VIP", Player.Name + " is now Online.")
                else:
                    Server.Broadcast(Player.Name + " is now Online!")
        except:
            pass
 
    def On_PlayerDisconnected(self, Player):
        try:
            DataStore.Remove("MaxHomes", Player.SteamID)
            DataStore.Remove("MTPCooldown", Player.SteamID)
            DataStore.Remove("VKitCooldown", Player.SteamID)
            DataStore.Remove("LVL1DKitCooldown", Player.SteamID)
            DataStore.Remove("LVL2DKitCooldown", Player.SteamID)
            DataStore.Remove("LVL1VKitCooldown", Player.SteamID)
            DataStore.Remove("LVL2VKitCooldown", Player.SteamID)
            DataStore.Remove("DTPCooldown", Player.SteamID)
            DataStore.Remove("ModBan", Player.SteamID)
            DataStore.Remove("MODLOCATION", Player.SteamID)
            if DataStore.Get("DonatorRank", "LeaveMSG") == "true":
                if Player.SteamID == DataStore.Get("DonatorRank", "OwnerID"):
                    Server.BroadcastFrom("Owner", Player.Name + " is now Offline.")
                elif Player.Admin:
                    Server.BroadcastFrom("Admin", Player.Name + " is now Offline.")
                elif self.isMod(Player):
                    Server.BroadcastFrom("Moderator", Player.Name + " is now Offline.")
                elif self.isDonator(Player):
                    Server.BroadcastFrom("Donator", Player.Name + " is now Offline.")
                elif self.isVIP(Player):
                    Server.BroadcastFrom("VIP", Player.Name + " is now Offline.")
                else:
                    Server.Broadcast(Player.Name + " is now Offline!")
        except:
            pass
 
    def On_Chat(self, Player, ChatMessage):
        #try:
        if DataStore.Get("DonatorRank", "ChatPrefix") == "true":
            if DataStore.Get("DonatorRank", "OwnerID") == str(Player.SteamID):
                chatmsg = str(ChatMessage)[1:-1]
                ocolour = DataStore.Get("DonatorRank", "OwnerColour")
                Server.BroadcastFrom("[Owner] ♚ " + Player.Name, ocolour + chatmsg)
                ChatMessage.NewText = "*%"
                return
            elif Player.Admin:
                chatmsg = str(ChatMessage)[1:-1]
                acolour = DataStore.Get("DonatorRank", "AdminColour")
                Server.BroadcastFrom("[Admin] ♚ " + Player.Name, acolour + chatmsg)
                ChatMessage.NewText = "*%"
            elif self.isMod(Player):
                chatmsg = str(ChatMessage)[1:-1]
                mcolour = DataStore.Get("DonatorRank", "ModColour")
                Server.BroadcastFrom("[Mod] ♚ " + Player.Name, mcolour + chatmsg)
                ChatMessage.NewText = "*%"
            elif self.isDonator(Player):
                chatmsg = str(ChatMessage)[1:-1]
                dcolour = DataStore.Get("DonatorRank", "DonatorColour")
                Server.BroadcastFrom("[Donator] ☠ " + Player.Name, dcolour + chatmsg)
                ChatMessage.NewText = "*%"
            elif self.isVIP(Player):
                chatmsg = str(ChatMessage)[1:-1]
                vcolour = DataStore.Get("DonatorRank", "VIPColour")
                Server.BroadcastFrom("[VIP] ☠ " + Player.Name, vcolour + chatmsg)
                ChatMessage.NewText = "*%"
        #except:
            #pass

    def isMod(self, Player):
        try:
            ini = self.getUserIni()
            if ini.GetSetting(Player.SteamID, "Rank") == "Mod":
                return True
            elif DataStore.ContainsKey("Moderators", Player.SteamID):
                if ini.GetSetting(Player.SteamID, "Rank") == "Mod":
                    return True
                d = Plugin.GetDate()
                t = Plugin.GetTime()
                ini.AddSetting(modname.SteamID, "UserName", modname.Name)
                ini.AddSetting(modname.SteamID, "INFO", "Time: " + t + "||Date: " + d + "||By: SERVER CONSOLE")
                ini.AddSetting(modname.SteamID, "Rank", "Mod")
                ini.AddSetting(modname.SteamID, "MaxHomes", DataStore.Get("DonatorRank", "ModHomesMax"))
                ini.AddSetting(modname.SteamID, "AddVIPS", "true")
                ini.AddSetting(modname.SteamID, "AddDonators", "true")
                ini.AddSetting(modname.SteamID, "AddMods", "false")
                ini.AddSetting(modname.SteamID, "DelVIPS", "true")
                ini.AddSetting(modname.SteamID, "DelDonators", "true")
                ini.AddSetting(modname.SteamID, "DelMods", "false")
                ini.AddSetting(modname.SteamID, "LVL1VKIT", "false")
                ini.AddSetting(modname.SteamID, "LVL2VKIT", "false")
                ini.AddSetting(modname.SteamID, "LVL1DKIT", "false")
                ini.AddSetting(modname.SteamID, "LVL2DKIT", "false")
                ini.AddSetting(modname.SteamID, "MODKIT", "true")
                ini.AddSetting(modname.SteamID, "CanKick", "true")
                ini.AddSetting(modname.SteamID, "CanBan", "true")
                ini.AddSetting(modname.SteamID, "VTP", "false")
                ini.AddSetting(modname.SteamID, "DTP", "false")
                ini.AddSetting(modname.SteamID, "MTP", "true")
                ini.AddSetting(modname.SteamID, "UseBroadcast", "true")
                ini.AddSetting(modname.SteamID, "AccessInfo", "true")
                ini.Save()
                return True
            else:
                return False
        except:
            pass
 
    def isDonator(self, Player):
        try:
            ini = self.getUserIni()
            if ini.GetSetting(Player.SteamID, "Rank") == "Donator":
                return True
            else:
                return None
        except:
            pass
 
    def isVIP(self, Player):
        try:
            ini = self.getUserIni()
            if ini.GetSetting(Player.SteamID, "Rank") == "VIP":
                return True
            else:
                return None
        except:
            pass
 
    def isBanned(self, Player):
        try:
            ini = self.BansListIni()
            if ini.GetSetting("BannedIPs", Player.IP) is not None:
                return True
            elif ini.GetSetting("BannedIDs", Player.SteamID) is not None:
                return True
            else:
                return None
        except:
            pass
 
    def GetSettingsIni(self):
        if not Plugin.IniExists("Settings"):
            ini = Plugin.CreateIni("Settings")
            ini.Save()
        return Plugin.GetIni("Settings")
 
    def getUserIni(self):
        if not Plugin.IniExists("Users"):
            ini = Plugin.CreateIni("Users")
            ini.Save()
        return Plugin.GetIni("Users")
 
    def getLogIni(self):
        if not Plugin.IniExists("Logs"):
            ini = Plugin.CreateIni("Logs")
            ini.Save()
        return Plugin.GetIni("Logs")
 
    def BansListIni(self):
        if not Plugin.IniExists("BansList"):
            ini = Plugin.CreateIni("BansList")
            ini.AddSetting("BannedIDs", "", "")
            ini.AddSetting("BannedIPs", "", "")
            ini.Save()
        return Plugin.GetIni("BansList")
 
    def On_PlayerHurt(self, hit):
        try:
            if self.TrytoGrabID(hit.Attacker) is None:
                return
            elif DataStore.Get("ModBan", hit.Attacker.SteamID) == "on":
                ini = self.BansListIni()
                hit.DamageAmount = 0
                ini.AddSetting("BannedIPs", hit.Victim.IP, hit.Victim.Name + " was banned by: " + hit.Attacker.Name)
                ini.AddSetting("BannedIDs", hit.Victim.SteamID, hit.Victim.Name + " was banned by: " + hit.Attacker.Name)
                ini.Save()
                Server.Broadcast("[color red]" + hit.Victim.Name + "[/color] has been banned by: [color red]" + hit.Attacker.Name)
                hit.Victim.Disconnect()
                DataStore.Remove("ModBan", hit.Attacker.SteamID)
                hit.Attacker.Message("You can now safely shoot another player")
        except:
            pass

 
    def argsToText(self, args):
        text = str.join(" ", args)
        return text
 
    #Method provided by Spoock. Converted to Python by DreTaX
    def CheckV(self, Player, args):
        count = 0
        if hasattr(args, '__len__') and (not isinstance(args, str)):
            p = self.GetPlayerName(str.join(" ", args))
            if p is not None:
                return p
            for pl in Server.Players:
                for namePart in args:
                    if namePart.lower() in pl.Name.lower():
                        p = pl
                        count += 1
                        continue
        else:
            nargs = str(args).lower()
            p = self.GetPlayerName(nargs)
            if p is not None:
                return p
            for pl in Server.ActivePlayers:
                if nargs in pl.Name.lower():
                    p = pl
                    count += 1
                    continue
        if count == 0:
            Player.Message("Couldn't find " + str.join(" ", args) + "!")
            return None
        elif count == 1 and p is not None:
            return p
        else:
            Player.Message("Found " + str(count) + " players with similar a name. Use a more correct name!")
            return None
 
    #GetPlayerName provided by DreTaX
    def GetPlayerName(self, name):
        try:
            name = name.lower()
            for pl in Server.Players:
                if pl.Name.lower() == name:
                    return pl
            return None
        except:
            return None

    def TrytoGrabID(self, Player):
        try:
            id = Player.SteamID
            return id
        except:
            return None

    def vkit1(self, sett, Player):
        #Will add an enum section loop here one day
        vkitinv1 = sett.GetSetting("VKIT_Level1", "Inv1")
        vkitinv2 = sett.GetSetting("VKIT_Level1", "Inv2")
        vkitinv3 = sett.GetSetting("VKIT_Level1", "Inv3")
        vkitinv4 = sett.GetSetting("VKIT_Level1", "Inv4")
        vkitinv5 = sett.GetSetting("VKIT_Level1", "Inv5")
        vkitinv6 = sett.GetSetting("VKIT_Level1", "Inv6")
        vkitinv7 = sett.GetSetting("VKIT_Level1", "Inv7")
        vkitinv8 = sett.GetSetting("VKIT_Level1", "Inv8")
        vkitinv9 = sett.GetSetting("VKIT_Level1", "Inv9")
        vkitinv10 = sett.GetSetting("VKIT_Level1", "Inv10")
        vkitinv11 = sett.GetSetting("VKIT_Level1", "Inv11")
        vkitinv12 = sett.GetSetting("VKIT_Level1", "Inv12")
        vkitinv13 = sett.GetSetting("VKIT_Level1", "Inv13")
        vkitinv14 = sett.GetSetting("VKIT_Level1", "Inv14")
        vkitinv15 = sett.GetSetting("VKIT_Level1", "Inv15")
        vkitinv16 = sett.GetSetting("VKIT_Level1", "Inv16")
        vkitinv17 = sett.GetSetting("VKIT_Level1", "Inv17")
        vkitinv18 = sett.GetSetting("VKIT_Level1", "Inv18")
        vkitinv19 = sett.GetSetting("VKIT_Level1", "Inv19")
        vkitinv20 = sett.GetSetting("VKIT_Level1", "Inv20")
        vkitqty1 = sett.GetSetting("VKIT_Level1", "Qty1")
        vkitqty2 = sett.GetSetting("VKIT_Level1", "Qty2")
        vkitqty3 = sett.GetSetting("VKIT_Level1", "Qty3")
        vkitqty4 = sett.GetSetting("VKIT_Level1", "Qty4")
        vkitqty5 = sett.GetSetting("VKIT_Level1", "Qty5")
        vkitqty6 = sett.GetSetting("VKIT_Level1", "Qty6")
        vkitqty7 = sett.GetSetting("VKIT_Level1", "Qty7")
        vkitqty8 = sett.GetSetting("VKIT_Level1", "Qty8")
        vkitqty9 = sett.GetSetting("VKIT_Level1", "Qty9")
        vkitqty10 = sett.GetSetting("VKIT_Level1", "Qty10")
        vkitqty11 = sett.GetSetting("VKIT_Level1", "Qty11")
        vkitqty12 = sett.GetSetting("VKIT_Level1", "Qty12")
        vkitqty13 = sett.GetSetting("VKIT_Level1", "Qty13")
        vkitqty14 = sett.GetSetting("VKIT_Level1", "Qty14")
        vkitqty15 = sett.GetSetting("VKIT_Level1", "Qty15")
        vkitqty16 = sett.GetSetting("VKIT_Level1", "Qty16")
        vkitqty17 = sett.GetSetting("VKIT_Level1", "Qty17")
        vkitqty18 = sett.GetSetting("VKIT_Level1", "Qty18")
        vkitqty19 = sett.GetSetting("VKIT_Level1", "Qty19")
        vkitqty20 = sett.GetSetting("VKIT_Level1", "Qty20")
        Player.Inventory.AddItem(vkitinv1, int(vkitqty1))
        Player.Inventory.AddItem(vkitinv2, int(vkitqty2))
        Player.Inventory.AddItem(vkitinv3, int(vkitqty3))
        Player.Inventory.AddItem(vkitinv4, int(vkitqty4))
        Player.Inventory.AddItem(vkitinv5, int(vkitqty5))
        Player.Inventory.AddItem(vkitinv6, int(vkitqty6))
        Player.Inventory.AddItem(vkitinv7, int(vkitqty7))
        Player.Inventory.AddItem(vkitinv8, int(vkitqty8))
        Player.Inventory.AddItem(vkitinv9, int(vkitqty9))
        Player.Inventory.AddItem(vkitinv10, int(vkitqty10))
        Player.Inventory.AddItem(vkitinv11, int(vkitqty11))
        Player.Inventory.AddItem(vkitinv12, int(vkitqty12))
        Player.Inventory.AddItem(vkitinv13, int(vkitqty13))
        Player.Inventory.AddItem(vkitinv14, int(vkitqty14))
        Player.Inventory.AddItem(vkitinv15, int(vkitqty15))
        Player.Inventory.AddItem(vkitinv16, int(vkitqty16))
        Player.Inventory.AddItem(vkitinv17, int(vkitqty17))
        Player.Inventory.AddItem(vkitinv18, int(vkitqty18))
        Player.Inventory.AddItem(vkitinv19, int(vkitqty19))
        Player.Inventory.AddItem(vkitinv20, int(vkitqty20))

    def vkit2(self, sett, Player):
        vkitinv1 = sett.GetSetting("VKIT_Level2", "Inv1")
        vkitinv2 = sett.GetSetting("VKIT_Level2", "Inv2")
        vkitinv3 = sett.GetSetting("VKIT_Level2", "Inv3")
        vkitinv4 = sett.GetSetting("VKIT_Level2", "Inv4")
        vkitinv5 = sett.GetSetting("VKIT_Level2", "Inv5")
        vkitinv6 = sett.GetSetting("VKIT_Level2", "Inv6")
        vkitinv7 = sett.GetSetting("VKIT_Level2", "Inv7")
        vkitinv8 = sett.GetSetting("VKIT_Level2", "Inv8")
        vkitinv9 = sett.GetSetting("VKIT_Level2", "Inv9")
        vkitinv10 = sett.GetSetting("VKIT_Level2", "Inv10")
        vkitinv11 = sett.GetSetting("VKIT_Level2", "Inv11")
        vkitinv12 = sett.GetSetting("VKIT_Level2", "Inv12")
        vkitinv13 = sett.GetSetting("VKIT_Level2", "Inv13")
        vkitinv14 = sett.GetSetting("VKIT_Level2", "Inv14")
        vkitinv15 = sett.GetSetting("VKIT_Level2", "Inv15")
        vkitinv16 = sett.GetSetting("VKIT_Level2", "Inv16")
        vkitinv17 = sett.GetSetting("VKIT_Level2", "Inv17")
        vkitinv18 = sett.GetSetting("VKIT_Level2", "Inv18")
        vkitinv19 = sett.GetSetting("VKIT_Level2", "Inv19")
        vkitinv20 = sett.GetSetting("VKIT_Level2", "Inv20")
        vkitqty1 = sett.GetSetting("VKIT_Level2", "Qty1")
        vkitqty2 = sett.GetSetting("VKIT_Level2", "Qty2")
        vkitqty3 = sett.GetSetting("VKIT_Level2", "Qty3")
        vkitqty4 = sett.GetSetting("VKIT_Level2", "Qty4")
        vkitqty5 = sett.GetSetting("VKIT_Level2", "Qty5")
        vkitqty6 = sett.GetSetting("VKIT_Level2", "Qty6")
        vkitqty7 = sett.GetSetting("VKIT_Level2", "Qty7")
        vkitqty8 = sett.GetSetting("VKIT_Level2", "Qty8")
        vkitqty9 = sett.GetSetting("VKIT_Level2", "Qty9")
        vkitqty10 = sett.GetSetting("VKIT_Level2", "Qty10")
        vkitqty11 = sett.GetSetting("VKIT_Level2", "Qty11")
        vkitqty12 = sett.GetSetting("VKIT_Level2", "Qty12")
        vkitqty13 = sett.GetSetting("VKIT_Level2", "Qty13")
        vkitqty14 = sett.GetSetting("VKIT_Level2", "Qty14")
        vkitqty15 = sett.GetSetting("VKIT_Level2", "Qty15")
        vkitqty16 = sett.GetSetting("VKIT_Level2", "Qty16")
        vkitqty17 = sett.GetSetting("VKIT_Level2", "Qty17")
        vkitqty18 = sett.GetSetting("VKIT_Level2", "Qty18")
        vkitqty19 = sett.GetSetting("VKIT_Level2", "Qty19")
        vkitqty20 = sett.GetSetting("VKIT_Level2", "Qty20")
        Player.Inventory.AddItem(vkitinv1, int(vkitqty1))
        Player.Inventory.AddItem(vkitinv2, int(vkitqty2))
        Player.Inventory.AddItem(vkitinv3, int(vkitqty3))
        Player.Inventory.AddItem(vkitinv4, int(vkitqty4))
        Player.Inventory.AddItem(vkitinv5, int(vkitqty5))
        Player.Inventory.AddItem(vkitinv6, int(vkitqty6))
        Player.Inventory.AddItem(vkitinv7, int(vkitqty7))
        Player.Inventory.AddItem(vkitinv8, int(vkitqty8))
        Player.Inventory.AddItem(vkitinv9, int(vkitqty9))
        Player.Inventory.AddItem(vkitinv10, int(vkitqty10))
        Player.Inventory.AddItem(vkitinv11, int(vkitqty11))
        Player.Inventory.AddItem(vkitinv12, int(vkitqty12))
        Player.Inventory.AddItem(vkitinv13, int(vkitqty13))
        Player.Inventory.AddItem(vkitinv14, int(vkitqty14))
        Player.Inventory.AddItem(vkitinv15, int(vkitqty15))
        Player.Inventory.AddItem(vkitinv16, int(vkitqty16))
        Player.Inventory.AddItem(vkitinv17, int(vkitqty17))
        Player.Inventory.AddItem(vkitinv18, int(vkitqty18))
        Player.Inventory.AddItem(vkitinv19, int(vkitqty19))
        Player.Inventory.AddItem(vkitinv20, int(vkitqty20))

    def dkit1(self, sett, Player):
        dkitinv1 = sett.GetSetting("DKIT_Level1", "Inv1")
        dkitinv2 = sett.GetSetting("DKIT_Level1", "Inv2")
        dkitinv3 = sett.GetSetting("DKIT_Level1", "Inv3")
        dkitinv4 = sett.GetSetting("DKIT_Level1", "Inv4")
        dkitinv5 = sett.GetSetting("DKIT_Level1", "Inv5")
        dkitinv6 = sett.GetSetting("DKIT_Level1", "Inv6")
        dkitinv7 = sett.GetSetting("DKIT_Level1", "Inv7")
        dkitinv8 = sett.GetSetting("DKIT_Level1", "Inv8")
        dkitinv9 = sett.GetSetting("DKIT_Level1", "Inv9")
        dkitinv10 = sett.GetSetting("DKIT_Level1", "Inv10")
        dkitinv11 = sett.GetSetting("DKIT_Level1", "Inv11")
        dkitinv12 = sett.GetSetting("DKIT_Level1", "Inv12")
        dkitinv13 = sett.GetSetting("DKIT_Level1", "Inv13")
        dkitinv14 = sett.GetSetting("DKIT_Level1", "Inv14")
        dkitinv15 = sett.GetSetting("DKIT_Level1", "Inv15")
        dkitinv16 = sett.GetSetting("DKIT_Level1", "Inv16")
        dkitinv17 = sett.GetSetting("DKIT_Level1", "Inv17")
        dkitinv18 = sett.GetSetting("DKIT_Level1", "Inv18")
        dkitinv19 = sett.GetSetting("DKIT_Level1", "Inv19")
        dkitinv20 = sett.GetSetting("DKIT_Level1", "Inv20")
        dkitqty1 = sett.GetSetting("DKIT_Level1", "Qty1")
        dkitqty2 = sett.GetSetting("DKIT_Level1", "Qty2")
        dkitqty3 = sett.GetSetting("DKIT_Level1", "Qty3")
        dkitqty4 = sett.GetSetting("DKIT_Level1", "Qty4")
        dkitqty5 = sett.GetSetting("DKIT_Level1", "Qty5")
        dkitqty6 = sett.GetSetting("DKIT_Level1", "Qty6")
        dkitqty7 = sett.GetSetting("DKIT_Level1", "Qty7")
        dkitqty8 = sett.GetSetting("DKIT_Level1", "Qty8")
        dkitqty9 = sett.GetSetting("DKIT_Level1", "Qty9")
        dkitqty10 = sett.GetSetting("DKIT_Level1", "Qty10")
        dkitqty11 = sett.GetSetting("DKIT_Level1", "Qty11")
        dkitqty12 = sett.GetSetting("DKIT_Level1", "Qty12")
        dkitqty13 = sett.GetSetting("DKIT_Level1", "Qty13")
        dkitqty14 = sett.GetSetting("DKIT_Level1", "Qty14")
        dkitqty15 = sett.GetSetting("DKIT_Level1", "Qty15")
        dkitqty16 = sett.GetSetting("DKIT_Level1", "Qty16")
        dkitqty17 = sett.GetSetting("DKIT_Level1", "Qty17")
        dkitqty18 = sett.GetSetting("DKIT_Level1", "Qty18")
        dkitqty19 = sett.GetSetting("DKIT_Level1", "Qty19")
        dkitqty20 = sett.GetSetting("DKIT_Level1", "Qty20")
        Player.Inventory.AddItem(dkitinv1, int(dkitqty1))
        Player.Inventory.AddItem(dkitinv2, int(dkitqty2))
        Player.Inventory.AddItem(dkitinv3, int(dkitqty3))
        Player.Inventory.AddItem(dkitinv4, int(dkitqty4))
        Player.Inventory.AddItem(dkitinv5, int(dkitqty5))
        Player.Inventory.AddItem(dkitinv6, int(dkitqty6))
        Player.Inventory.AddItem(dkitinv7, int(dkitqty7))
        Player.Inventory.AddItem(dkitinv8, int(dkitqty8))
        Player.Inventory.AddItem(dkitinv9, int(dkitqty9))
        Player.Inventory.AddItem(dkitinv10, int(dkitqty10))
        Player.Inventory.AddItem(dkitinv11, int(dkitqty11))
        Player.Inventory.AddItem(dkitinv12, int(dkitqty12))
        Player.Inventory.AddItem(dkitinv13, int(dkitqty13))
        Player.Inventory.AddItem(dkitinv14, int(dkitqty14))
        Player.Inventory.AddItem(dkitinv15, int(dkitqty15))
        Player.Inventory.AddItem(dkitinv16, int(dkitqty16))
        Player.Inventory.AddItem(dkitinv17, int(dkitqty17))
        Player.Inventory.AddItem(dkitinv18, int(dkitqty18))
        Player.Inventory.AddItem(dkitinv19, int(dkitqty19))
        Player.Inventory.AddItem(dkitinv20, int(dkitqty20))

    def dkit2(self, sett, Player):
        dkitinv1 = sett.GetSetting("DKIT_Level2", "Inv1")
        dkitinv2 = sett.GetSetting("DKIT_Level2", "Inv2")
        dkitinv3 = sett.GetSetting("DKIT_Level2", "Inv3")
        dkitinv4 = sett.GetSetting("DKIT_Level2", "Inv4")
        dkitinv5 = sett.GetSetting("DKIT_Level2", "Inv5")
        dkitinv6 = sett.GetSetting("DKIT_Level2", "Inv6")
        dkitinv7 = sett.GetSetting("DKIT_Level2", "Inv7")
        dkitinv8 = sett.GetSetting("DKIT_Level2", "Inv8")
        dkitinv9 = sett.GetSetting("DKIT_Level2", "Inv9")
        dkitinv10 = sett.GetSetting("DKIT_Level2", "Inv10")
        dkitinv11 = sett.GetSetting("DKIT_Level2", "Inv11")
        dkitinv12 = sett.GetSetting("DKIT_Level2", "Inv12")
        dkitinv13 = sett.GetSetting("DKIT_Level2", "Inv13")
        dkitinv14 = sett.GetSetting("DKIT_Level2", "Inv14")
        dkitinv15 = sett.GetSetting("DKIT_Level2", "Inv15")
        dkitinv16 = sett.GetSetting("DKIT_Level2", "Inv16")
        dkitinv17 = sett.GetSetting("DKIT_Level2", "Inv17")
        dkitinv18 = sett.GetSetting("DKIT_Level2", "Inv18")
        dkitinv19 = sett.GetSetting("DKIT_Level2", "Inv19")
        dkitinv20 = sett.GetSetting("DKIT_Level2", "Inv20")
        dkitqty1 = sett.GetSetting("DKIT_Level2", "Qty1")
        dkitqty2 = sett.GetSetting("DKIT_Level2", "Qty2")
        dkitqty3 = sett.GetSetting("DKIT_Level2", "Qty3")
        dkitqty4 = sett.GetSetting("DKIT_Level2", "Qty4")
        dkitqty5 = sett.GetSetting("DKIT_Level2", "Qty5")
        dkitqty6 = sett.GetSetting("DKIT_Level2", "Qty6")
        dkitqty7 = sett.GetSetting("DKIT_Level2", "Qty7")
        dkitqty8 = sett.GetSetting("DKIT_Level2", "Qty8")
        dkitqty9 = sett.GetSetting("DKIT_Level2", "Qty9")
        dkitqty10 = sett.GetSetting("DKIT_Level2", "Qty10")
        dkitqty11 = sett.GetSetting("DKIT_Level2", "Qty11")
        dkitqty12 = sett.GetSetting("DKIT_Level2", "Qty12")
        dkitqty13 = sett.GetSetting("DKIT_Level2", "Qty13")
        dkitqty14 = sett.GetSetting("DKIT_Level2", "Qty14")
        dkitqty15 = sett.GetSetting("DKIT_Level2", "Qty15")
        dkitqty16 = sett.GetSetting("DKIT_Level2", "Qty16")
        dkitqty17 = sett.GetSetting("DKIT_Level2", "Qty17")
        dkitqty18 = sett.GetSetting("DKIT_Level2", "Qty18")
        dkitqty19 = sett.GetSetting("DKIT_Level2", "Qty19")
        dkitqty20 = sett.GetSetting("DKIT_Level2", "Qty20")
        Player.Inventory.AddItem(dkitinv1, int(dkitqty1))
        Player.Inventory.AddItem(dkitinv2, int(dkitqty2))
        Player.Inventory.AddItem(dkitinv3, int(dkitqty3))
        Player.Inventory.AddItem(dkitinv4, int(dkitqty4))
        Player.Inventory.AddItem(dkitinv5, int(dkitqty5))
        Player.Inventory.AddItem(dkitinv6, int(dkitqty6))
        Player.Inventory.AddItem(dkitinv7, int(dkitqty7))
        Player.Inventory.AddItem(dkitinv8, int(dkitqty8))
        Player.Inventory.AddItem(dkitinv9, int(dkitqty9))
        Player.Inventory.AddItem(dkitinv10, int(dkitqty10))
        Player.Inventory.AddItem(dkitinv11, int(dkitqty11))
        Player.Inventory.AddItem(dkitinv12, int(dkitqty12))
        Player.Inventory.AddItem(dkitinv13, int(dkitqty13))
        Player.Inventory.AddItem(dkitinv14, int(dkitqty14))
        Player.Inventory.AddItem(dkitinv15, int(dkitqty15))
        Player.Inventory.AddItem(dkitinv16, int(dkitqty16))
        Player.Inventory.AddItem(dkitinv17, int(dkitqty17))
        Player.Inventory.AddItem(dkitinv18, int(dkitqty18))
        Player.Inventory.AddItem(dkitinv19, int(dkitqty19))
        Player.Inventory.AddItem(dkitinv20, int(dkitqty20))