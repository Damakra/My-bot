from ayarlar import ayarlar
import discord
# import * - kütüphanedeki tüm dosyaları içe aktarmanın hızlı bir yoludur
from bot_mantik import sifre_olusturucu
from bot_mantik import emoji_olusturucu
from bot_mantik import yazi_tura
from resim_gonderme import get_duck_image_url





# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
ayricaliklar = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
ayricaliklar.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
istemci = discord.Client(intents=ayricaliklar)


# Bot hazır olduğunda adını yazdıracak!
@istemci.event
async def on_ready():
    print(f'{istemci.user} olarak giriş yaptık')


# Bot bir mesaj aldığında, aynı kanalda mesaj gönderecek!
@istemci.event
async def on_message(message):
    if message.author == istemci.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Selam!')
    
    elif message.content.startswith("$bye"):
        await message.channel.send("Hoşçakal! :slight_smile:")
    
    elif message.content.startswith("$help"):
        await message.channel.send("Hemen anlatayım, bana yazmak istediğinde herşeyin önüne '$' işaretini koy, işte yazabileciğin komutlar! : hello (Bana selam vermek için.), bye (Hoşçakal demek için.), help (Yardım almak için.), smile (Raskele gülümseyen emoji atmam için.), coin (Yazı tura oynamak için.), pass (Şifre oluşturmak için.). Bu kadar basit!! ")

    elif message.content.startswith('$smile'):
        await message.channel.send(emoji_olusturucu())
    
    elif message.content.startswith('$coin'):
        await message.channel.send(yazi_tura())
    
    elif message.content.startswith('$duck'):
        await message.channel.send(get_duck_image_url())
    
    elif message.content.startswith('$pass'):
        await message.channel.send(sifre_olusturucu(10))
    
    elif message.content.startswith('$karton değerlendirme'):
        await message.channel.send('Bir karton kutuyu değerlendirmek istiyorsan evde bu karton kutunun içerisine katılmayı bekleyen herhangi bir şeyi koya bilirsin sıvı hariç tabiki yoksa karton eriye bilir. Bunun dışında eğer elinde sadece bir veya birden fazla karton varsa internette bu kartonu kullana bileceğin fikirlere baka bilirsin, pek çok kişi bu karton ile kutu, telefon tutacağı, kalemlik veya eğerki çok ileri gitmek istersen küçük bir sehpa bile yapabilirsin hatta bir kitaplık bile, veyatta küçük figürlerde yapabilirsin senin için fikir bulabileceğin bir pinterest listesini buraya bırakıyorum!! https://tr.pinterest.com/semrayilmazoglu/karton-kutu-de%C4%9Ferlendirme/')
    
    elif message.content.startswith("$cam değerlendirme"):
        await message.channel.send("Camı değerlendirme işi biraz tehlikeli özellikle eğerki kırıksa eğerki cam kırık ise güvenlik açısından camı iki poşet veya karton bir kutunun içerisine koyun, bunu yaptıktan sonra en yakın geri dönüşüme atın hangi geri dönüşüme atacağınızı bilmiyorsanız bota '$cam geri dönüşüm' yazın. Bunun dışında cam bir kutuyu veya cam bir şişenin içine herhangi birşey katıp saklaya bilirsiniz.  Bir cam geri dönüştürüldüğünde : yemek kavanozları, içecek şişeleri, kozmetik ambalajlar vb. olabilir.")
    
    elif message.content.startswith("$plastikleri değerlendirme"):
        await message.channel.send("plastikleri değerlendirmede şişe veya kutu değilse geri dönüşüme atılmalıdır. Camın hangi geri dönüşüme atılacağını bilmiyorsanız '$plastik geri dönüşüm' yazın.")
    
    elif message.content.startswith('$kağıt geri dönüşüm'):
        await message.channel.send("Neredeyse tüm kağıt türleri geri dönüştürülebilir. Kağıt geri dönüşüm kutularında genel olarak kabul edilmeyen kağıt öğeler arasında kahverengi zarflar ve kraft zarflar, karbon kağıtlar, kağıt havlular, mendiller, şeker ambalajları, kahve fincanları ve pizza kutuları bulunur.")

    elif message.content.startswith('$cam geri dönüşüm'):
        await message.channel.send("Tüm cam atıklar geri dönüştürülebilmektedir. Ancak bazı atık camlar ağır metaller veya zararlı gazlar içerdikleri için tehlikeli atık sınıfına, ya da hastanelerde tedavi amaçlı kullanılan ilaçları içeren bazı şişeler de tıbbi atık sınıfına girmektedir. Bu nedenle florasanlar, ampuller, cam tesisi arıtma çamuru (cam tozu) ve hastanelerde çıkan filakon şişeler gibi camların geri dönüştürülmesi için lisanslı araçlarla toplanması ve tehlikeli atık ya da tıbbi atık işleme tesisi lisansına sahip tesislerde işlenmesi gerekmektedir. ")

    elif message.content.startswith('$plastik geri dönüşüm'):
        await message.channel.send("Bütün Plastikler geri dönüştürülemez. Güneş gözlükleri kurşun geçirmez ürünler ve bazı su şişeleri bu tür plastik malzemelerden üretilirler. Bu malzemelerin geri dönüşümü yapılamamaktadır.")
    
    else:
        await message.channel.send("Bu komutu anlayamadım :(, başka bir şey dene!")





    
istemci.run(ayarlar["TOKEN"])





