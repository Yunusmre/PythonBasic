from json import load, dump, dumps

#Json Dosyasına veri yazdırma
def jsonWrite(fileName, data):
    try:
        with open(fileName, "w", encoding="UTF-8") as f:
            dump(data, f, ensure_ascii=False, indent=6)
            f.close()
    except Exception as ex:
        print(f"Hata Türü: {type(ex).__name__}\nHata Mesajı: {ex}\nHata Kodu: JWE0")

#Json Dosyasını Okuma
def jsonLoad(fileName, writeLayout = 0):
    try:
        with open(fileName, "r", encoding="UTF-8") as f:
            data = load(f)
            f.close()
        
        return dumps(data, indent=writeLayout)
    except Exception as ex:
        print(f"Hata Türü: {type(ex).__name__}\nHata Mesajı: {ex}\nHata Kodu: JLE0")

#Json Dosyasına Veri Ekleme
def jsonAdd(fileName, data, writeAgain = False, writeLayout = 0):
    try:
        with open(fileName, "r", encoding="UTF-8") as f:
            oldData = load(f)
            f.close()
        
        oldData.update(data)

        if (writeAgain): jsonWrite(fileName, oldData)
        return dumps(oldData, indent=writeLayout)
    
    except Exception as ex:
        print(f"Hata Türü: {type(ex).__name__}\nHata Mesajı: {ex}\nHata Kodu: JAE0")
