from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivymd.app import MDApp
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivymd.uix.list import MDList, OneLineAvatarListItem, ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

# Dimensioni finestra
Window.size = (360, 640)

class MainMenu(Screen):
    pass

class CharactersScreen(Screen):
    def build(self):
        pass

class MapScreen(Screen):
   def build(self):
       pass
   

class EthisScreen(Screen):
    def build(self):
        pass

class FostScreen(Screen):
    def build(self):
        pass

class GoldbrickScreen(Screen):
    def build(self):
        pass

class KharDurimScreen(Screen):
    def build(self):
        pass

class KurkScreen(Screen):
    def build(self):
        pass

class LaboratorioScreen(Screen):
    def build(self):
        pass

class NorthpearlScreen(Screen):
    def build(self):
        pass

class OgaldukScreen(Screen):
    def build(self):
        pass

class ValdenorScreen(Screen):
    def build(self):
        pass

class VingaldrumScreen(Screen):
    def build(self):
        pass



class DanvarScreen(Screen):
    def build(self):
        pass

class MicarScreen(Screen):
    def build(self):
        pass

class DraxelScreen(Screen):
    def build(self):
        pass

class InferionScreen(Screen):
    def build(self):
        pass

class LudwigScreen(Screen):
    def build(self):
        pass

class ThogarScreen(Screen):
    def build(self):
        pass

class BalokScreen(Screen):
    def build(self):
        pass

class GhorScreen(Screen):
    def build(self):
        pass

class BhorScreen(Screen):
    def build(self):
        pass

class MorakScreen(Screen):
    def build(self):
        pass

class XanderCaelScreen(Screen):
    def build(self):
        pass

class EldranKelthornScreen(Screen):
    def build(self):
        pass

class BalinTorfardScreen(Screen):
    def build(self):
        pass

class TommyTorfardScreen(Screen):
    def build(self):
        pass

class BrenfordScreen(Screen):
    def build(self):
        pass

class CarlyleScreen(Screen):
    def build(self):
        pass

class DaliaScreen(Screen):
    def build(self):
        pass

class IvanBlackswordScreen(Screen):
    def build(self):
        pass

class DurganScreen(Screen):
    def build(self):
        pass

class DorianThalorScreen(Screen):
    def build(self):
        pass

class ThorgrimScreen(Screen):
    def build(self):
        pass

class LaeNorielScreen(Screen):
    def build(self):
        pass

class TalNorielScreen(Screen):
    def build(self):
        pass

class EthelindraScreen(Screen):
    def build(self):
        pass

class EthelindorScreen(Screen):
    def build(self):
        pass

class SiriusScreen(Screen):
    def build(self):
        pass

class ValasScreen(Screen):
    def build(self):
        pass

class SoluunScreen(Screen):
    def build(self):
        pass

class ZaelRithScreen(Screen):
    def build(self):
        pass

class VorakNyxaraScreen(Screen):
    def build(self):
        pass

class KallithScreen(Screen):
    def build(self):
        pass

class MirellaScreen(Screen):
    def build(self):
        pass

class TharimScreen(Screen):
    def build(self):
        pass

class AlzarethScreen(Screen):
    def build(self):
        pass

class PippinScreen(Screen):
    def build(self):
        pass

class ArkhanScreen(Screen):
    def build(self):
        pass

class IvorScreen(Screen):
    def build(self):
        pass

class ArlinScreen(Screen):
    def build(self):
        pass


class LoreScreen(Screen):
    def build(self):
        pass


class EthelindraETalNorielScreen(Screen):
    def build(self):
        pass


class NascitaDiVingaldrumScreen(Screen):
    def build(self):
        pass 

class LeggendaDiKurkScreen(Screen):
    def build(self):
        pass

class DinastieDiKurkScreen(Screen):
    def build(self):
        pass

class BattagliaDiFostScreen(Screen):
    def build(self):
        pass

class GenesiDiIshusScreen(Screen):
    def build(self):
        pass

class SessioniScreen(Screen):
    def build(self):
        pass



class DnDApp(MDApp):
    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "700"

        Builder.load_file("mainmenu.kv")  

        Builder.load_file("personaggi/characters.kv")
        Builder.load_file("personaggi/dettagli/protagonisti/danvar.kv")
        Builder.load_file("personaggi/dettagli/protagonisti/micar.kv")
        Builder.load_file("personaggi/dettagli/protagonisti/draxel.kv")
        Builder.load_file("personaggi/dettagli/protagonisti/inferion.kv")
        Builder.load_file("personaggi/dettagli/protagonisti/ludwig.kv")
        Builder.load_file("personaggi/dettagli/protagonisti/thogar.kv")
        Builder.load_file("personaggi/dettagli/protagonisti/balok.kv")

        Builder.load_file("personaggi/dettagli/clan/ghor.kv")
        Builder.load_file("personaggi/dettagli/clan/bhor.kv")
        Builder.load_file("personaggi/dettagli/clan/morak.kv")

        Builder.load_file("personaggi/dettagli/goldbrick/xander.kv")
        Builder.load_file("personaggi/dettagli/goldbrick/eldran.kv")
        Builder.load_file("personaggi/dettagli/goldbrick/balin.kv")
        Builder.load_file("personaggi/dettagli/goldbrick/tommy.kv")
        Builder.load_file("personaggi/dettagli/goldbrick/brenford.kv")
        Builder.load_file("personaggi/dettagli/goldbrick/carlyle.kv")
        Builder.load_file("personaggi/dettagli/goldbrick/dalia.kv")
        Builder.load_file("personaggi/dettagli/goldbrick/ivan.kv")
        Builder.load_file("personaggi/dettagli/goldbrick/dorian.kv")
        Builder.load_file("personaggi/dettagli/goldbrick/durgan.kv")

        Builder.load_file("personaggi/dettagli/thorgrim/thorgrim.kv")

        Builder.load_file("personaggi/dettagli/vingaldrum/laenoriel.kv")
        Builder.load_file("personaggi/dettagli/vingaldrum/talnoriel.kv")
        Builder.load_file("personaggi/dettagli/vingaldrum/ethelindra.kv")
        Builder.load_file("personaggi/dettagli/vingaldrum/ethelindor.kv")

        Builder.load_file("personaggi/dettagli/kurk/sirius.kv")

        Builder.load_file("personaggi/dettagli/bregan/valas.kv")
        Builder.load_file("personaggi/dettagli/bregan/soluun.kv")

        Builder.load_file("personaggi/dettagli/isothar/zaelrith.kv")
        Builder.load_file("personaggi/dettagli/isothar/vorak.kv")

        Builder.load_file("personaggi/dettagli/laboratorio/kallith.kv")
        Builder.load_file("personaggi/dettagli/laboratorio/mirella.kv")
        Builder.load_file("personaggi/dettagli/laboratorio/tharim.kv")
        Builder.load_file("personaggi/dettagli/laboratorio/alzareth.kv")

        Builder.load_file("personaggi/dettagli/ethis/pippin.kv")
        Builder.load_file("personaggi/dettagli/ethis/arkhan.kv")
        Builder.load_file("personaggi/dettagli/ethis/ivor.kv")
        Builder.load_file("personaggi/dettagli/ethis/arlin.kv")

        Builder.load_file("luoghi/map.kv")

        Builder.load_file("luoghi/dettagli/ethis.kv")
        Builder.load_file("luoghi/dettagli/fost.kv")
        Builder.load_file("luoghi/dettagli/goldbrick.kv")
        Builder.load_file("luoghi/dettagli/khardurim.kv")
        Builder.load_file("luoghi/dettagli/kurk.kv")
        Builder.load_file("luoghi/dettagli/laboratorio.kv")
        Builder.load_file("luoghi/dettagli/northpearl.kv")
        Builder.load_file("luoghi/dettagli/ogalduk.kv")
        Builder.load_file("luoghi/dettagli/valdenor.kv")
        Builder.load_file("luoghi/dettagli/vingaldrum.kv")

        Builder.load_file("lore/lore.kv")

        Builder.load_file("lore/dettagli/ethelindra_e_talnoriel.kv")
        Builder.load_file("lore/dettagli/nascita_di_vingaldrum.kv")
        Builder.load_file("lore/dettagli/leggenda_di_kurk.kv")
        Builder.load_file("lore/dettagli/dinastie_di_kurk.kv")
        Builder.load_file("lore/dettagli/battaglia_di_fost.kv")
        Builder.load_file("lore/dettagli/genesi_di_ishus.kv")




        self.sm = ScreenManager(transition=FadeTransition())
        self.sm.add_widget(MainMenu(name="menu"))
        self.sm.add_widget(CharactersScreen(name="characters"))
        self.sm.add_widget(DanvarScreen(name="danvar"))
        self.sm.add_widget(MicarScreen(name="micar"))
        self.sm.add_widget(DraxelScreen(name="draxel"))
        self.sm.add_widget(InferionScreen(name="inferion"))
        self.sm.add_widget(LudwigScreen(name="ludwig"))
        self.sm.add_widget(ThogarScreen(name="thogar"))
        self.sm.add_widget(BalokScreen(name="balok"))

        self.sm.add_widget(GhorScreen(name="ghor"))
        self.sm.add_widget(BhorScreen(name="bhor"))
        self.sm.add_widget(MorakScreen(name="morak"))

        self.sm.add_widget(XanderCaelScreen(name="xander"))
        self.sm.add_widget(EldranKelthornScreen(name="eldran"))
        self.sm.add_widget(BalinTorfardScreen(name="balin"))
        self.sm.add_widget(TommyTorfardScreen(name="tommy"))
        self.sm.add_widget(BrenfordScreen(name="brenford"))
        self.sm.add_widget(CarlyleScreen(name="carlyle"))
        self.sm.add_widget(DaliaScreen(name="dalia"))
        self.sm.add_widget(IvanBlackswordScreen(name="ivan"))
        self.sm.add_widget(DorianThalorScreen(name="dorian"))
        self.sm.add_widget(DurganScreen(name="durgan"))

        self.sm.add_widget(ThorgrimScreen(name="thorgrim"))

        self.sm.add_widget(LaeNorielScreen(name="laenoriel"))
        self.sm.add_widget(TalNorielScreen(name="talnoriel"))
        self.sm.add_widget(EthelindraScreen(name="ethelindra"))
        self.sm.add_widget(EthelindorScreen(name="ethelindor"))

        self.sm.add_widget(SiriusScreen(name="sirius"))

        self.sm.add_widget(ValasScreen(name="valas"))
        self.sm.add_widget(SoluunScreen(name="soluun"))

        self.sm.add_widget(ZaelRithScreen(name="zaelrith"))
        self.sm.add_widget(VorakNyxaraScreen(name="vorak"))

        self.sm.add_widget(KallithScreen(name="kallith"))
        self.sm.add_widget(MirellaScreen(name="mirella"))
        self.sm.add_widget(TharimScreen(name="tharim"))
        self.sm.add_widget(AlzarethScreen(name="alzareth"))

        self.sm.add_widget(PippinScreen(name="pippin"))
        self.sm.add_widget(ArkhanScreen(name="arkhan"))
        self.sm.add_widget(IvorScreen(name="ivor"))
        self.sm.add_widget(ArlinScreen(name="arlin"))

        self.sm.add_widget(MapScreen(name="map"))

        self.sm.add_widget(EthisScreen(name="ethis"))
        self.sm.add_widget(FostScreen(name="fost"))
        self.sm.add_widget(GoldbrickScreen(name="goldbrick"))
        self.sm.add_widget(KharDurimScreen(name="khardurim"))
        self.sm.add_widget(KurkScreen(name="kurk"))
        self.sm.add_widget(LaboratorioScreen(name="laboratorio"))
        self.sm.add_widget(NorthpearlScreen(name="northpearl"))
        self.sm.add_widget(OgaldukScreen(name="ogalduk")) 
        self.sm.add_widget(ValdenorScreen(name="valdenor"))
        self.sm.add_widget(VingaldrumScreen(name="vingaldrum"))

        self.sm.add_widget(LoreScreen(name="lore"))

        self.sm.add_widget(EthelindraETalNorielScreen(name="ethelindra_e_talnoriel"))
        self.sm.add_widget(NascitaDiVingaldrumScreen(name="nascita_di_vingaldrum"))
        self.sm.add_widget(LeggendaDiKurkScreen(name="leggenda_di_kurk"))
        self.sm.add_widget(DinastieDiKurkScreen(name="dinastie_di_kurk"))
        self.sm.add_widget(BattagliaDiFostScreen(name="battaglia_di_fost"))
        self.sm.add_widget(GenesiDiIshusScreen(name="genesi_di_ishus"))


        return self.sm

    def animate_button(self, button):
        if button.size_hint_x is not None and button.size_hint_y is not None:
            anim = Animation(size_hint=(0.9, None), duration=0.3) + Animation(size_hint=(0.8, None), duration=0.3)
            anim.start(button)

    def change_screen(self, screen_name):
        self.sm.current = screen_name  

if __name__ == "__main__":
    DnDApp().run()
