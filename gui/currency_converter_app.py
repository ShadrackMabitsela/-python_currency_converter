import pathlib
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "newproject"


class CurrencyConverterApp:
    def __init__(self, master=None):
        # build ui
        self.tl_main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.frm_main = tk.Frame(self.tl_main_window)
        self.btn_converter = tk.Button(self.frm_main)
        self.btn_converter.configure(
            background="#000000", foreground="#FFFFFF", text="Convert Currency"
        )
        self.btn_converter.place(anchor="nw", relx="0.63", rely="0.85", x="0", y="0")
        self.cmb_currencies_1 = ttk.Combobox(self.frm_main)
        self.cmb_currencies_1.configure(justify="left", values="val1")
        self.cmb_currencies_1.place(
            anchor="nw",
            bordermode="inside",
            height="30",
            relx="0.45",
            rely="0.45",
            width="200",
            x="0",
            y="0",
        )
        self.cmb_currencies_2 = ttk.Combobox(self.frm_main)
        self.cmb_currencies_2.configure(justify="left", values="val1")
        self.cmb_currencies_2.place(
            anchor="nw",
            bordermode="inside",
            height="30",
            relx="0.45",
            rely="0.65",
            width="200",
            x="0",
            y="0",
        )
        self.entry_1 = tk.Entry(self.frm_main)
        self.entry_1.configure(
            background="#000000", borderwidth="3", cursor="xterm", foreground="#FFFFFF"
        )
        self.entry_1.configure(justify="left", selectbackground="#404040")
        self.entry_1.place(
            anchor="nw", height="35", relx="0.0", rely="0.45", width="150", x="0", y="0"
        )
        self.entry_2 = tk.Entry(self.frm_main)
        self.entry_2.configure(
            background="#000000", borderwidth="3", cursor="xterm", foreground="#FFFFFF"
        )
        self.entry_2.configure(justify="left", selectbackground="#404040")
        self.entry_2.place(
            anchor="nw", height="35", relx="0.0", rely="0.65", width="150", x="0", y="0"
        )
        self.lbl_details = ttk.Label(self.frm_main)
        self.lbl_details.configure(
            background="#000000",
            foreground="#FFFFFF",
            justify="left",
            text="Test Text.",
        )
        self.lbl_details.place(anchor="nw", height="100", width="370", x="0", y="0")
        self.lbl_date = ttk.Label(self.frm_main)
        self.lbl_date.configure(
            background="#000000",
            foreground="#FFFFFF",
            justify="left",
            text="Test Text.",
        )
        self.lbl_date.place(
            anchor="nw", height="28", rely="0.3", width="370", x="0", y="0"
        )
        self.frm_main.configure(
            background="#000000", height="400", padx="10", pady="10"
        )
        self.frm_main.configure(takefocus=False, width="400")
        self.frm_main.place(anchor="nw", x="0", y="0")
        self.tl_main_window.configure(background="#000000", height="400", width="400")
        self.tl_main_window.resizable(False, False)
        self.tl_main_window.title("Currency Converter")
        self.tl_main_window.pack_propagate(0)

        # Main widget
        self.mainwindow = self.tl_main_window

    def run(self):
        self.mainwindow.mainloop()
