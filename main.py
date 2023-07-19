import creopyson as cp

# c = creopyson.Client()
# c.connect()
# print ("Sprawdź czy Serwer Creoson i Creo Parametric jest uruchomiony!")
# c.creo_set_creo_version(7)
# c.dimension_set("wymiar",200)
# c.parameter_set("parametr", value = "VK_PR_P02")
# print ("Zmiany będą widoczne po regeneracji modelu CTRL+g")
# c.creo_cd("C:\Users\Admin\Desktop\vk_pr_p02")
# c.file_load_material_file("Ferrous_metals", "C:/Program Files/PTC/Creo 7.0.1.0/Common Files/text/materials-library/Standard-Materials_Granta-Design")
# c.file_set_cur_material( "Ferrous_metal")
# c.file_regenerate()

def main():
    material_path = "C:\Program Files\PTC\Creo 7.0.1.0\Common Files\\text\materials-library\Standard-Materials_Granta-Design\Ferrous_metals"
    directory_path = "C:\Work\Api"
    c = cp.Client()
    c.connect()
    c.creo_set_creo_version(7)
    c.creo_cd(directory_path)

    v = int(input("Wpisz wartosc v:\n"))
    while (v < 0) :
        print("Wartosc nie moze byc mniejsza niz 0, podaj poprawna wartosc")
        w = int(input("Wpisz wartosc w: "))

    k = int(input("Wpisz wartosc k:\n"))
    while (k < 0):
        print("Wartosc nie moze byc mniejsza niz 0, podaj poprawna wartosc")
        l = int(input("Wpisz wartosc l"))
    h = int(input("Wpisz wartosc h:\n"))
    while (h < 0):
        print("Wartosc nie moze byc mniejsza niz 0, podaj poprawna wartosc")
        h = int(input("Wpisz wartosc h"))
    t_h = int(input("Wpisz wartosc t_h:\n"))
    while (t_h < 0 or t_h > h):
        print("Wartosc jest mniejsza niz 0 lub wieksza od h, podaj poprawna wartosc")
        t_h = int(input("Wpisz wartosc t_h"))
    t_l = int(input("Wpisz wartosc t_l:\n"))
    while (t_l < 0):
        print("Wartosc nie moze byc mniejsza niz 0, podaj wartosc poprawna")
        t_l = int(input("Wpisz wartosc t_l"))
    t_w = int(input("Wpisz wartosc t_w:\n"))
    parameter = input("Wpisz wartosc parametru (string)")
    materialy = {1: "Cast_iron_ductile.mtl", 2: "Cast_iron_gray.mtl", 3: "Cast_iron_malleable.mtl"
                 , 4: "Cast_iron_nodular.mtl", 5: "Stainless_steel_austenitic.mtl", 6: "Stainless_steel_ferritic.mtl",
                 7: "Stainless_steel_martensitic.mtl", 8: "Steel_cast.mtl", 9: "Steel_galvanized.mtl",
                 10: "Steel_high_carbon.mtl"}
    print("Wybierz numer materialu (od 1 do 10):")
    for keys, values in materialy.items():
        print(keys, values)
    material_name = int(input())

    c.dimension_set("v", value=v)
    c.dimension_set("k", value=k)
    c.dimension_set("h", value=h)
    c.dimension_set("t_h", value=t_h)
    c.dimension_set("t_l", value=t_l)
    c.dimension_set("t_w", value=t_w)
    c.parameter_set("PARAMETER", value=parameter)
    c.file_load_material_file(materialy[material_name], material_path)
    c.file_set_cur_material(materialy[material_name])
    c.file_regenerate()

if __name__ == "__main__":
    main();