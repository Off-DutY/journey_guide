#!/usr/bin/env python3
"""Update plan.json navigation URLs with verified coordinate-based Google Maps URLs."""
import json

def maps_url(lat, lng):
    return f"https://maps.google.com/?q={lat},{lng}"

# All verified coordinates
verified = {
    "taoyuan_t2":            (25.0773, 121.2322),
    "blue_car_rental_kef":   (63.9932, -22.6056),
    "refurinn_guesthouse":   (64.1505, -21.9457),
    "harpa":                 (64.1504, -21.9326),
    "sun_voyager":           (64.1476, -21.9223),
    "skolavourdustigur":     (64.1459, -21.9326),
    "hallgrimskirkja":       (64.1417, -21.9266),
    "tjornin":               (64.1415, -21.9426),
    "perlan":                (64.1294, -21.9191),
    "sky_lagoon":            (64.1158, -21.9411),
    "aurora_hotel":          (63.9983, -22.6298),
    "blue_lagoon":           (63.8814, -22.4531),
    "thingvellir":           (64.2560, -21.1298),
    "bruarfoss_parking":     (64.2402, -20.5238),
    "geysir":                (64.3138, -20.2995),
    "gullfoss":              (64.3223, -20.1193),
    "kerid":                 (64.0413, -20.8851),
    "arhus_cottage":         (63.8331, -20.4064),
    "seljalandsfoss":        (63.6159, -19.9928),
    "solheimajokull":        (63.5304, -19.3704),
    "skogafoss":             (63.5321, -19.5112),
    "reynisfjara":           (63.4044, -19.0453),
    "farmhouse_lodge":       (63.4376, -19.1898),
    "vik_meeting_point":     (63.4188, -19.0069),
    "jokulasarlon":          (64.0784, -16.2306),
    "saudanes_guesthouse":   (64.2807, -15.1515),
    "viking_village":        (64.2494, -14.9961),
    "viking_cafe":           (64.2446, -14.9720),
    "hofn":                  (64.2539, -15.2082),
    "langabud":              (64.6569, -14.2901),
    "eggin_gledivik":        (64.6618, -14.2948),
    "djupivogur":            (64.6562, -14.2849),
    "bulandstindur":         (64.6050, -14.2600),
    "gufufoss":              (65.2555, -14.0133),
    "seydisfjordur":         (65.2601, -14.0058),
    "herard_hotel":          (65.2669, -14.3948),
    "vok_baths":             (65.3039, -14.4493),
    "namafjall_hverir":      (65.6381, -16.8173),
    "krafla_viti":           (65.7153, -16.7650),
    "myvatn_nature_baths":   (65.6317, -16.8497),
    "grjotagja_parking":     (65.6261, -16.8823),
    "hverfell_parking":      (65.6090, -16.8776),
    "dimmuborgir":           (65.5916, -16.9129),
    "skutustadagigar":       (65.5709, -17.0347),
    "godafoss":              (65.6828, -17.5502),
    "hotel_north":           (65.7003, -18.0834),
    "akureyri_city":         (65.6835, -18.0878),
    "akureyrarkirkja":       (65.6827, -18.0906),
    "blonduoskirkja":        (65.6597, -20.2805),
    "vatnsdalsholar":        (65.5018, -20.3788),
    "budardalur":            (65.1049, -21.7651),
    "kirkjufell_mountain":   (64.9274, -23.3052),
    "kirkjufell_guesthouse": (64.9215, -23.2589),
    "ingjaldsholl_church":   (64.9228, -23.9128),
    "geirabakari":           (64.5409, -21.9090),  # Borgarnes
    "bridge_between_continents": (63.8114, -22.6680),
    "citybox_oslo":          (59.9121, 10.7478),
    "fiskeriet_youngstorget": (59.9149, 10.7488),
    "gudvangen_fjordtell":   (60.8806, 6.8415),
    "vangen_cafe_voss":      (60.6270, 6.4190),
    "zander_k_hotel":        (60.3910, 5.3275),
    "scandic_falkoner":      (55.6808, 12.5262),
    "appartcity_brussels":   (50.8388, 4.3360),
    "chez_leon":             (50.8480, 4.3530),
    "hotel_ibis_amsterdam_west": (52.3922, 4.8498),
    # Landmarks
    "oslo_s":                (59.9116, 10.7501),
    "oslo_opera":            (59.9074, 10.7531),
    "myrdal_station":        (60.7268, 7.1308),
    "flam_station":          (60.8634, 7.1168),
    "flam_dock":             (60.8624, 7.1194),
    "gudvangen":             (60.8765, 6.8335),
    "voss_station":          (60.6288, 6.4161),
    "bergen_station":        (60.3913, 5.3325),
    "floibanen":             (60.3929, 5.3268),
    "mostraumen":            (60.3948, 5.3195),
    "bryggen":               (60.3975, 5.3219),
    "fisketorget_bergen":    (60.3946, 5.3252),
    "bergen_aquarium":       (60.3978, 5.2987),
    "lille_lungegardsvann":  (60.3873, 5.3367),
    "bergen_airport":        (60.2934, 5.2185),
    "tollbodallmenningen":   (60.3960, 5.3243),
    "little_mermaid":        (55.6929, 12.5994),
    "amalienborg":           (55.6840, 12.5934),
    "nyhavn":                (55.6798, 12.5908),
    "stroget":               (55.6779, 12.5800),
    "rundetarn":             (55.6813, 12.5748),
    "cph_airport":           (55.6180, 12.6561),
    "canal_tours_cph":       (55.6770, 12.5762),
    "galeries_saint_hubert": (50.8472, 4.3551),
    "grand_place":           (50.8467, 4.3525),
    "manneken_pis":          (50.8451, 4.3500),
    "mont_des_arts":         (50.8449, 4.3578),
    "royal_palace_brussels": (50.8419, 4.3625),
    "brussels_south":        (50.8358, 4.3358),
    "brussels_airport":      (50.9014, 4.4844),
    "bruges_station":        (51.1977, 3.2165),
    "church_our_lady_bruges": (51.2051, 3.2233),
    "nepomucenus_bridge":    (51.2049, 3.2258),
    "bruges_markt":          (51.2090, 3.2244),
    "canal_boat_bruges":     (51.2073, 3.2229),
    "half_moon_brewery":     (51.2023, 3.2245),
    "begijnhof_bruges":      (51.2014, 3.2237),
    "cinquantenaire":        (50.8408, 4.3952),
    "amsterdam_centraal":    (52.3792, 4.9003),
    "giethoorn":             (52.7392, 6.0803),
    "keukenhof":             (52.2700, 4.5469),
    "van_gogh_museum":       (52.3584, 4.8811),
    "rijksmuseum":           (52.3600, 4.8852),
    "amsterdam_canal":       (52.3769, 4.8999),
    "schiphol":              (52.3105, 4.7683),
    # Crystal Ice Cave meeting point (Vatnajökull - near Jökulsárlón)
    "crystal_ice_cave_meeting": (64.0784, -16.2306),
}


def get_key(ti, day_id):
    """Map event title + day context to a verified coordinate key."""
    # Day 1 - Taiwan / KEF arrival
    if "桃園機場第二航廈" in ti or "第二航廈" in ti:
        return "taoyuan_t2"
    if "Blue Car Rental" in ti:
        return "blue_car_rental_kef"
    if "Refurinn" in ti:
        return "refurinn_guesthouse"

    # Reykjavik landmarks
    if "Harpa" in ti:
        return "harpa"
    if "Sun Voyager" in ti or "太陽航海者" in ti:
        return "sun_voyager"
    if "Skólavörðustígur" in ti or "Skolavourdustigur" in ti or "彩虹街" in ti:
        return "skolavourdustigur"
    if "Hallgrímskirkja" in ti or "Hallgrimskirkja" in ti or "大教堂" in ti:
        return "hallgrimskirkja"
    if "Tjörnin" in ti or "Tjornin" in ti or "市政廳湖" in ti:
        return "tjornin"
    if "Perlan" in ti or "珍珠樓" in ti:
        return "perlan"
    if "Sky Lagoon" in ti:
        return "sky_lagoon"
    if "Aurora Hotel" in ti or "極光酒店" in ti:
        return "aurora_hotel"
    if "Blue Lagoon" in ti or "藍湖" in ti:
        return "blue_lagoon"

    # Golden Circle
    if "Þingvellir" in ti or "Thingvellir" in ti or "辛格韋德利" in ti:
        return "thingvellir"
    if "Brúarfoss" in ti or "Bruarfoss" in ti:
        return "bruarfoss_parking"
    if "Geysir" in ti or "間歇泉" in ti:
        return "geysir"
    if "Gullfoss" in ti or "黃金瀑布" in ti:
        return "gullfoss"
    if "Kerið" in ti or "Kerid" in ti or "火山湖" in ti:
        return "kerid"
    if "Árnes" in ti or "Arhus Cottage" in ti or "Arnes" in ti:
        return "arhus_cottage"

    # South coast
    if "Seljalandsfoss" in ti or "瀑布" in ti and day_id in (4, 5):
        pass  # fall through for Skogafoss check first
    if "Seljalandsfoss" in ti:
        return "seljalandsfoss"
    if "Sólheimajökull" in ti or "Solheimajokull" in ti or "索爾黑馬冰川" in ti:
        return "solheimajokull"
    if "Skógafoss" in ti or "Skogafoss" in ti:
        return "skogafoss"
    if "Reynisfjara" in ti or "雷尼斯菲亞拉" in ti or "黑沙灘" in ti:
        return "reynisfjara"
    if "Farmhouse Lodge" in ti or "農莊" in ti:
        return "farmhouse_lodge"
    if "集合點" in ti or "Katla Ice Cave" in ti:
        return "vik_meeting_point"

    # East Iceland
    if "Jökulsárlón" in ti or "Jokulasarlon" in ti or "冰河湖" in ti:
        return "jokulasarlon"
    if "Sauðanes" in ti or "Saudanes" in ti:
        return "saudanes_guesthouse"
    if "Viking Village" in ti or "維京村" in ti:
        return "viking_village"
    if "Viking Café" in ti or "Viking Cafe" in ti or "維京咖啡" in ti:
        return "viking_cafe"
    if "Höfn" in ti or "Hofn" in ti or "霍芬" in ti:
        return "hofn"
    if "Langabúð" in ti or "Langabud" in ti:
        return "langabud"
    if "Eggið í gleðivík" in ti or "Eggin" in ti or "Eggid" in ti:
        return "eggin_gledivik"
    if "Djúpivogur" in ti or "Djupivogur" in ti:
        return "djupivogur"
    if "Búlandstindur" in ti or "Bulandstindur" in ti:
        return "bulandstindur"
    if "Gufufoss" in ti:
        return "gufufoss"
    if "Seyðisfjörður" in ti or "Seydisfjordur" in ti:
        return "seydisfjordur"
    if "Hérað" in ti or "Herard" in ti or "Herad" in ti:
        return "herard_hotel"
    if "Vök Baths" in ti or "Vok Baths" in ti:
        return "vok_baths"

    # North Iceland / Myvatn
    if "Námafjall" in ti or "Namafjall" in ti or "Hverir" in ti:
        return "namafjall_hverir"
    if "Krafla" in ti or "Viti" in ti and "Krafla" in ti:
        return "krafla_viti"
    if "Mývatn Nature Baths" in ti or "Myvatn Nature Baths" in ti or "米湖溫泉" in ti:
        return "myvatn_nature_baths"
    if "Grjótagjá" in ti or "Grjotagja" in ti:
        return "grjotagja_parking"
    if "Hverfell" in ti or "Hverfjall" in ti:
        return "hverfell_parking"
    if "Dimmuborgir" in ti or "黑暗城堡" in ti:
        return "dimmuborgir"
    if "Skútustaðagígar" in ti or "Skutustadagigar" in ti or "偽火山口" in ti:
        return "skutustadagigar"
    if "Goðafoss" in ti or "Godafoss" in ti or "眾神瀑布" in ti:
        return "godafoss"
    if "Hotel North" in ti or "北方酒店" in ti:
        return "hotel_north"
    if "Akureyri" in ti and ("城市" in ti or "市區" in ti or "Church" in ti or "大教堂" not in ti):
        return "akureyri_city"
    if "Akureyrarkirkja" in ti or ("Akureyri" in ti and "大教堂" in ti):
        return "akureyrarkirkja"
    if "Blönduós" in ti or "Blonduos" in ti or "Blönduóskirkja" in ti:
        return "blonduoskirkja"
    if "Vatnsdalshólar" in ti or "Vatnsdalsholar" in ti:
        return "vatnsdalsholar"
    if "Búðardalur" in ti or "Budardalur" in ti:
        return "budardalur"

    # Crystal Ice Cave meeting point (near Jökulsárlón)
    if "Crystal Ice Cave" in ti or "水晶冰洞" in ti:
        return "crystal_ice_cave_meeting"

    # Vestrahorn (Batman Mountain) - navigate to Viking Cafe at Stokksnes entrance
    if "Vestrahorn" in ti or "西角山" in ti or "蝙蝠山" in ti:
        return "viking_cafe"

    # West Iceland / Snæfellsnes
    if "Kirkjufell" in ti and ("山" in ti or "Mountain" in ti or "瀑布" in ti or "Waterfall" in ti):
        return "kirkjufell_mountain"
    if "Kirkjufell" in ti and ("Guesthouse" in ti or "住宿" in ti or "民宿" in ti):
        return "kirkjufell_guesthouse"
    if "Kirkjufell" in ti:
        return "kirkjufell_mountain"
    if "Ingjaldshóll" in ti or "Ingjaldsholl" in ti:
        return "ingjaldsholl_church"
    if "Geirabakari" in ti or "麵包" in ti and "Borgarnes" in ti:
        return "geirabakari"
    if "Bridge Between Continents" in ti or "兩大洲橋" in ti or "大陸橋" in ti:
        return "bridge_between_continents"

    # Norway
    if "CityBox Oslo" in ti or "Citybox Oslo" in ti or "寄放行李" in ti and "Oslo" in ti:
        return "citybox_oslo"
    if "Flytoget" in ti:
        return "oslo_s"  # Flytoget arrives at Oslo Central Station
    if "市區巡禮" in ti and day_id == 12:
        return "oslo_opera"  # Oslo city tour reference point
    if "Oslo S" in ti or "奧斯陸中央車站" in ti:
        return "oslo_s"
    if "Oslo Opera" in ti or "奧斯陸歌劇院" in ti:
        return "oslo_opera"
    if "Fiskeriet" in ti or "Youngstorget" in ti:
        return "fiskeriet_youngstorget"
    if "Bergen Railway" in ti or "卑爾根鐵路" in ti:
        return "oslo_s"  # Departs from Oslo S
    if "Myrdal" in ti or "米達爾" in ti:
        return "myrdal_station"
    if "Flåm" in ti or "Flam" in ti:
        if "碼頭" in ti or "Dock" in ti or "pier" in ti.lower():
            return "flam_dock"
        return "flam_station"
    if "Gudvangen Fjordtell" in ti or "古德萬根峽灣旅館" in ti:
        return "gudvangen_fjordtell"
    if "走到高速公路" in ti or "搭乘點" in ti:
        return "gudvangen"  # Near Gudvangen bus pickup
    if "Gudvangen" in ti:
        return "gudvangen"
    if "Vangen Café" in ti or "Vangen Cafe" in ti or "Voss" in ti and "咖啡" in ti:
        return "vangen_cafe_voss"
    if "Voss" in ti and ("Station" in ti or "車站" in ti):
        return "voss_station"
    if "Zander K" in ti:
        return "zander_k_hotel"
    if "飯店吃早餐" in ti and "退房" in ti and day_id == 14:
        return "gudvangen_fjordtell"  # Breakfast & checkout at Gudvangen Fjordtell
    if "飯店吃早餐" in ti and day_id == 15:
        return "zander_k_hotel"  # Breakfast at Zander K Hotel Bergen
    if "飯店吃早餐" in ti and "退房" in ti and day_id == 16:
        return "zander_k_hotel"  # Checkout from Zander K Hotel Bergen
    if "前往搭乘纜車" in ti:
        return "floibanen"  # Bergen cable car (Fløibanen) lower station
    if "晚餐" in ti and "返回飯店" in ti and day_id == 14:
        return "zander_k_hotel"  # Bergen - return to Zander K Hotel
    if "晚餐" in ti and "返回飯店" in ti and day_id == 15:
        return "zander_k_hotel"  # Bergen - return to Zander K Hotel
    if "回住宿拿行李" in ti:
        return "zander_k_hotel"  # Pick up luggage at Zander K Hotel Bergen
    if "抵達卑爾根車站" in ti or ("Bergen" in ti and ("Station" in ti or "車站" in ti)):
        return "bergen_station"
    if "Fløibanen" in ti or "Floibanen" in ti or "纜車" in ti and "Bergen" in ti:
        return "floibanen"
    if "Mostraumen" in ti or "木斯特拉" in ti:
        return "mostraumen"
    if "Bryggen" in ti or "布呂根" in ti:
        return "bryggen"
    if "Fisketorget" in ti or "魚市場" in ti:
        return "fisketorget_bergen"
    if "水族館" in ti or "Bergen Aquarium" in ti or "卑爾根水族館" in ti:
        return "bergen_aquarium"
    if "Lille Lung" in ti or "Lungegard" in ti or "公園散步" in ti and "Lund" in ti:
        return "lille_lungegardsvann"
    if "Bergen Airport" in ti or "卑爾根" in ti and "機場" in ti or "BGO" in ti:
        return "bergen_airport"
    if "Tollbodallmenningen" in ti:
        return "tollbodallmenningen"

    # Denmark
    if "Scandic Falkoner" in ti:
        return "scandic_falkoner"
    if "Little Mermaid" in ti or "小美人魚" in ti:
        return "little_mermaid"
    if "Amalienborg" in ti or "阿美琳堡" in ti:
        return "amalienborg"
    if "Nyhavn" in ti or "新港" in ti:
        return "nyhavn"
    if "Strøget" in ti or "Stroget" in ti or "步行街" in ti:
        return "stroget"
    if "Rundetårn" in ti or "Rundetarn" in ti or "圓塔" in ti:
        return "rundetarn"
    if "Copenhagen Airport" in ti or "哥本哈根機場" in ti or "CPH" in ti:
        return "cph_airport"
    if "Canal Tours" in ti:
        # Day 17 = Copenhagen, Day 23 = Amsterdam
        if day_id == 17:
            return "canal_tours_cph"
        return "amsterdam_canal"
    if "運河遊船" in ti:
        if day_id <= 19:
            return "canal_boat_bruges"
        return "amsterdam_canal"

    # Belgium
    if "Appartcity" in ti or "Appart'City" in ti or "Appart" in ti and "Confort" in ti:
        return "appartcity_brussels"
    if "Chez Léon" in ti or "Chez Leon" in ti:
        return "chez_leon"
    if "Galeries Saint-Hubert" in ti or "聖胡伯特長廊" in ti or "聖休伯特" in ti:
        return "galeries_saint_hubert"
    if "Grand Place" in ti or "大廣場" in ti:
        return "grand_place"
    if "Manneken Pis" in ti or "尿尿小童" in ti:
        return "manneken_pis"
    if "Mont des Arts" in ti or "藝術山" in ti or "藝術之丘" in ti:
        return "mont_des_arts"
    if "Royal Palace" in ti or "王宮" in ti and "布魯塞爾" in ti:
        return "royal_palace_brussels"
    if "Brussels-South" in ti or "Brussels South" in ti or "布魯塞爾南站" in ti:
        return "brussels_south"
    if "歐洲之星" in ti or "Eurostar" in ti:
        return "brussels_south"  # Departs from Brussels-South
    if "前往月台等候" in ti:
        return "brussels_south"  # Waiting at Brussels-South platform for Eurostar
    if "拿行李" in ti and day_id == 20:
        return "appartcity_brussels"  # Pick up luggage at Appart'City Brussels
    if "Brussels Airport" in ti or "布魯塞爾機場" in ti:
        return "brussels_airport"
    if "前往 Bruges" in ti or "前往Bruges" in ti or "前往布魯日" in ti:
        return "bruges_station"
    if "Bruges" in ti and ("Station" in ti or "車站" in ti):
        return "bruges_station"
    if "前往火車站" in ti and day_id == 19:
        return "bruges_station"
    if "Church of Our Lady" in ti or "聖母教堂" in ti or "Onze-Lieve-Vrouwekerk" in ti:
        if day_id == 19:
            return "church_our_lady_bruges"
    if "Nepomucenus" in ti or ("橋" in ti and day_id == 19):
        return "nepomucenus_bridge"
    if "鐘樓" in ti and day_id == 19:
        return "bruges_markt"  # Belfry is at the Markt
    if "市集廣場" in ti and day_id == 19:
        return "bruges_markt"
    if "Bruges Markt" in ti or ("Markt" in ti and day_id == 19):
        return "bruges_markt"
    if "Canal Boat" in ti and "Bruges" in ti:
        return "canal_boat_bruges"
    if "Half Moon Brewery" in ti or "半月啤酒廠" in ti:
        return "half_moon_brewery"
    if "Begijnhof" in ti or "貝吉納修道院" in ti or "貝居安" in ti:
        return "begijnhof_bruges"
    if "Cinquantenaire" in ti or "五十週年紀念公園" in ti:
        return "cinquantenaire"
    if "布魯塞爾市區半日遊" in ti:
        return "grand_place"  # Brussels city tour - Grand Place as reference point

    # Netherlands
    if "Amsterdam Centraal" in ti or "阿姆斯特丹中央車站" in ti:
        return "amsterdam_centraal"
    if "返回阿姆斯特丹" in ti:
        return "amsterdam_centraal"
    if "Giethoorn" in ti or "羊角村" in ti:
        return "giethoorn"
    if "回程" in ti and day_id == 21:
        return "giethoorn"  # Return from Giethoorn day trip
    if "Keukenhof" in ti or "庫肯霍夫" in ti:
        return "keukenhof"
    if "Van Gogh Museum" in ti or "梵谷博物館" in ti:
        return "van_gogh_museum"
    if "Rijksmuseum" in ti or "國家博物館" in ti:
        return "rijksmuseum"
    if "Amsterdam Canal" in ti or "阿姆斯特丹運河" in ti:
        return "amsterdam_canal"
    if "最後購物" in ti:
        return "rijksmuseum"  # Amsterdam last shopping day - Rijksmuseum area as reference
    if "Schiphol" in ti or "史基浦機場" in ti:
        return "schiphol"
    if "Hotel ibis Amsterdam" in ti or "Hotel Ibis Amsterdam" in ti or "宜必思酒店" in ti:
        return "hotel_ibis_amsterdam_west"

    return None


def update_navigation(data):
    updated = 0
    skipped = 0
    no_match = []

    for day_idx, day in enumerate(data):
        day_id = day_idx + 1
        for event in day.get("events", []):
            ti = event.get("ti", "")
            key = get_key(ti, day_id)

            if key and key in verified:
                lat, lng = verified[key]
                new_url = maps_url(lat, lng)
                if event.get("navigation") != new_url:
                    event["navigation"] = new_url
                    updated += 1
            else:
                nav = event.get("navigation", "")
                if nav:
                    # Keep existing URL but note it as unmatched
                    no_match.append(f"Day {day_id}: {ti}")
                    skipped += 1

    return updated, skipped, no_match


with open("plan.json", encoding="utf-8") as f:
    data = json.load(f)

updated, skipped, no_match = update_navigation(data)

with open("plan.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Updated: {updated} events")
print(f"Skipped (no match): {skipped} events")
if no_match:
    print("\nUnmatched events (kept existing URL):")
    for m in no_match:
        print(f"  {m}")
