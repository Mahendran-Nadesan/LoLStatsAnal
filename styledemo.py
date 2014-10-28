# File: Tkthemes.py
# References:
#    http://www.tcl.tk/man/tcl8.5/TkCmd/Tk_style.htm

from Tkinter import *
from Tkinter import Tk
from demopanels import MsgPanel, SeeDismissPanel

class ThemeDemo(Tk.Frame):
    
    def __init__(self, isapp=True, name='themesdemo'):
        Tk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Tk Theme Demo')
        self.isapp = isapp
        self._create_widgets()
        
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self, 
                     ["Tk is the new Tk themed widget set. This is a Tk themed label, ",
                      "and below are three groups of Tk widgets in Tk labelframes.\n\n",
                      "The first group are all buttons that set the current application ",
                      "theme when pressed. Note the message box does not change as it uses ",
                      "a standard tkinter Label to hold the message.\n",
                      "The second group contains three sets of checkbuttons, ",
                      "with a separator widget between the sets. ",
                      "Note that the 'Enabled' button controls whether or not all the other ",
                      "buttons are in the disabled state.\n",
                      "The third group has a collection of linked radiobuttons."])
            
            SeeDismissPanel(self)
        
        self._create_demo_panel()
        self.allBtns = self.Tkbut + self.cbs[1:] + self.rb

        
    def _create_demo_panel(self):
        demoPanel = Tk.Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
        
        themePane = self._theme_pane(demoPanel)
        rbPane = self._rb_pane(demoPanel)
        cbPane = self._cb_pane(demoPanel)
        varPane = self._var_panel(demoPanel)
        
        themePane.pack(side=LEFT, expand=True, padx=10, pady=10, fill=BOTH)
        cbPane.pack(side=LEFT, expand=True, padx=10, pady=10,fill=BOTH)
        rbPane.pack(side=LEFT, expand=True, padx=10, pady=10, fill=BOTH)
        varPane.pack(side=LEFT, expand=True, padx=10, pady=10, fill=BOTH)
        
    def _theme_pane(self, parent):
        lf = Tk.Labelframe(parent, text='Themes')
        
        themes = sorted(Tk.Style().theme_names())
        self.Tkbut = []
        for t in themes:
            b = Tk.Button(lf, text=t, command=lambda t=t: Tk.Style().theme_use(t))
            b.pack(pady=2)
            self.Tkbut.append(b)
        
        return lf    
            
    def _cb_pane(self, parent):
        lf = Tk.Labelframe(parent, text='Checkbuttons')
        
        # control variables
        self.enabled = IntVar()
        self.cheese = IntVar()
        self.tomato = IntVar()
        self.basil = IntVar()
        self.oregano = IntVar()
        
        # checkbuttons
        self.cbOpt = Tk.Checkbutton(lf, text='Enabled', variable=self.enabled, command=self._toggle_opt)
        cbCheese = Tk.Checkbutton(text='Cheese', variable=self.cheese, command=self._show_vars)
        cbTomato = Tk.Checkbutton(text='Tomato', variable=self.tomato, command=self._show_vars)
        sep1 = Tk.Separator(orient=HORIZONTAL)
        cbBasil = Tk.Checkbutton(text='Basil', variable=self.basil, command=self._show_vars)
        cbOregano = Tk.Checkbutton(text='Oregano', variable=self.oregano, command=self._show_vars)
        sep2 = Tk.Separator(orient=HORIZONTAL)
        
        self.cbs = [self.cbOpt, sep1, cbCheese, cbTomato, sep2, cbBasil, cbOregano]
        for opt in self.cbs:
            if opt.winfo_class() == 'TCheckbutton':
                opt.configure(onvalue=1, offvalue=0)
                opt.setvar(opt.cget('variable'), 0)
                
            opt.pack(in_=lf, side=TOP, fill=X, pady=2, padx=5, anchor=W)
                    
        return lf

    def _rb_pane(self, parent):
        lf = Tk.Labelframe(parent, text='Radiobuttons', labelanchor=N+S)
            
        self.rb=[]
        self.happiness = StringVar()
        for s in ['Great', 'Good', 'OK', 'Poor', 'Awful']:
            b = Tk.Radiobutton(lf, text=s, value=s, 
                                variable=self.happiness,
                                command=lambda s=s: self._show_vars())
            b.pack(side=TOP, fill=X, pady=2)
            self.rb.append(b)
    
        return lf

    def _var_panel(self, parent):
        # panel to display check button variable values
        right = Tk.LabelFrame(parent, text='Control Variables')
        
        self.vb0 = Tk.Label(right, font=('Courier', 10))
        self.vb1 = Tk.Label(right, font=('Courier', 10))
        self.vb2 = Tk.Label(right, font=('Courier', 10))    
        self.vb3 = Tk.Label(right, font=('Courier', 10))  
        self.vb4 = Tk.Label(right, font=('Courier', 10))
        self.vb5 = Tk.Label(right, font=('Courier', 10))
        
        self.vb0.pack(anchor=NW, pady=3)
        self.vb1.pack(anchor=NW, pady=3)
        self.vb2.pack(anchor=NW, pady=3)
        self.vb3.pack(anchor=NW, pady=3)  
        self.vb4.pack(anchor=NW, pady=3)
        self.vb5.pack(anchor=NW, pady=3)
        
        self._show_vars()   
        
        return right

    def _show_vars(self):
        # set text for labels in var_panel to include the control 
        # variable name and current variable value
        self.vb0['text'] = '{:<11} {:<8}'.format('enabled:', self.enabled.get())
        self.vb1['text'] = '{:<11} {:<8}'.format('cheese:', self.cheese.get())
        self.vb2['text'] = '{:<11} {:<8}'.format('tomato:', self.tomato.get())
        self.vb3['text'] = '{:<11} {:<8}'.format('basil:', self.basil.get())
        self.vb4['text'] = '{:<11} {:<8}'.format('oregano:', self.oregano.get())
        self.vb4['text'] = '{:<11} {:<8}'.format('happiness:', self.happiness.get())

    def _toggle_opt(self):
        # state of the option buttons controlled
        # by the state of the Option frame label widget
        
        for opt in self.allBtns:
            if opt.winfo_class() != 'TSeparator':
                if self.cbOpt.instate(('selected', )):
                    opt['state'] = '!disabled'  # enable option
                else:
                    opt['state'] = 'disabled'
                    
        self._show_vars()

if __name__ == '__main__':
    ThemeDemo().mainloop()
