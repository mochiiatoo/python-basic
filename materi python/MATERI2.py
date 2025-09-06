print("----- MATERI 7C -----")

game_ridho = {"genshin", "mlbb", "delta", "hok" }
game_abdul = {"pubg", "mlbb", "hok"}
#.add()=> menambakan item ke set
game_ridho.add("pubg")
game_abdul.add("hok")
#.remove untuk menghapus item set
game_abdul.remove("mlbb")
# len() menghitung jumlah set
print("ridho ada:", len(game_ridho), "=>", game_ridho)
print("abdul ada:", len(game_abdul), "=>", game_abdul)
#.union() menggabungkan 2 set berbeda
game_gabungan = game_abdul.union(game_ridho)
total_game = len(game_gabungan)
print("game gabungan", total_game, "=>", game_gabungan )
#.intersection() mencari 2 item kembar dari set yang berbeda
#.difference() mencari item yang beda dari 2 set berbeda
game_kembar = game_ridho.intersection(game_abdul)
game_beda = game_ridho.difference(game_abdul)
print("game kembar:", game_kembar)
print("game beda:", game_beda)
# dict (dictionary)  -> {key:value}/ {kunci:isinya}
# berurutan berdasarkan key, berubah, key tidak duplikat
daftar_manhwa ={
    "hero killer": "ehwa",
    "killer peter": "peter",
    "999 wooden stick": "peach",
    "best girl": {
        "999 wooden stick": "kapten love",
        "killer peter": "nathaniel",
        "hero killer": "ehwa"
    }

    
}
print("daftar manhwa:", daftar_manhwa)
print("MC HERO KILLER:", daftar_manhwa["hero killer"])
print("best girl:", daftar_manhwa["best girl"]["hero killer"])
# mengubah item value berdasarkan key
daftar_manhwa["hero killer"] = "smiling man"
daftar_manhwa["best girl"]["killer peter"] = "nathaniel"
print("MC HERO KILLER BARU:", daftar_manhwa["hero killer"])
print("best girl cantik and imut:", daftar_manhwa["best girl"]["killer peter"])
# menambah item value berdasarkan key
daftar_manhwa["good bad fortune"] = "areka"
print("MC GOOD BAD FORTUNE:", daftar_manhwa['good bad fortune'])