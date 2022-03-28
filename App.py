import tkinter as tk
import hashlib as hash


def makeit(text):
    if(var.get()=="md5"):
        return hash.md5(text.encode()).hexdigest()
    elif(var.get()=="sha1"):
        return hash.sha1(text.encode()).hexdigest()
    elif(var.get()=="sha256"):
        return hash.sha256(text.encode()).hexdigest()

def hashed():
    text = txt_before.get()
    lbl_gen["text"] = makeit(text)

def hashedRes():
    text = txt_after.get()
    lbl_out["text"] = makeit(text)

def copyb():
    text = txt_before.get()
    txt_after.delete(0,tk.END)
    txt_after.insert(0,text)

def verifiez():
    hash1 = lbl_gen["text"]
    hash2 = lbl_out["text"]
    if(hash1==hash2):
        lbl["text"] = "The same hash"
    else:
        lbl["text"] = "Not the same hash"
def dest():
    window.destroy()
    exit(0)

window = tk.Tk()
window.columnconfigure(index=[0,1],weight=1)
window.rowconfigure(index=[0,1],weight=1)

window.title("Integrating Service")
frm1 = tk.Frame(master=window,height=15,width=1000)
frm1.columnconfigure(index=[0],weight=1)
frm1.rowconfigure(index=[0,1,2,3,4],weight=1)
lbl_desc_before = tk.Label(master=frm1,text='Message a decrypté:',width=45)
txt_before = tk.Entry(master=frm1)
lbl_hash_before = tk.Label(master=frm1,text="Hash : ")
lbl_gen = tk.Label(master=frm1,text="Empty")
btn_gen = tk.Button(master=frm1,text="genérie",command=hashed)
lbl_desc_before.pack(fill=tk.Y)
txt_before.pack()
lbl_hash_before.pack()
lbl_gen.pack()
btn_gen.pack()

empty = tk.Frame(master=window,height=15,width=120)


hashingtypes = ["md5","sha1","sha256"]
lbl = tk.Label(master=empty,text="",fg="red")
var = tk.StringVar(master=empty)
var.set(hashingtypes[0])
opt = tk.OptionMenu(empty,var,*hashingtypes)
opt.pack()
lbl.pack()

frm2 = tk.Frame(master=window,height=15,width=120)
frm2.columnconfigure(index=[0,1,2,3],weight=1)
frm2.columnconfigure(index=[0,1,2,3],weight=1)


fram2_1 = tk.Frame(master=frm2)

lbl_desc_after = tk.Label(master=fram2_1,text='Message a vérifier: ')
txt_after = tk.Entry(master=fram2_1)
lbl_after = tk.Label(master=fram2_1,text="Hash : ")
lbl_out = tk.Label(master=fram2_1,text="")

lbl_desc_after.pack()
txt_after.pack()
lbl_after.pack()
lbl_out.pack()

fram2_2 = tk.Frame(master=frm2)
btn_cpy = tk.Button(master=fram2_2,text="Copy", command=copyb)
btn_cpy.grid(column=0,row=0,sticky="news")
btn_g = tk.Button(master=fram2_2,text="Génerer",command=hashedRes)
btn_g.grid(column=1,row=0,sticky="news")
btn_v = tk.Button(master=fram2_2,text="Vérifier",command=verifiez)
btn_v.grid(column=2,row=0,sticky="news")
btn_t = tk.Button(master=fram2_2,text="Términer",command=dest)
btn_t.grid(column=3,row=0,sticky="news")

fram2_1.grid(row=0,sticky="news",padx=20,pady=20)
fram2_2.grid(row=1,sticky="news",padx=20,pady=20)

frm1.grid(column=0,row=0,sticky="nw")
empty.grid(column=1,row=0,sticky="n")
frm2.grid(column=2,row=0,sticky="ne")

window.mainloop()
