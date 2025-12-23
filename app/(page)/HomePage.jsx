import { useState } from "react";
import { SafeAreaView, StyleSheet, Text, View } from "react-native";
import BukuFavorit from "../../components/HomeScreen/BukuFavorit";
import CariBuku from "../../components/HomeScreen/CariBuku";
import KategoriTema from "../../components/tema/KategoriTema";

const HomePage = () => {
  const dataKategori = [
    { id: "matematika", name: "Matematika" },
    { id: "novel", name: "Novel" },
    { id: "komputer", name: "Komputer" },
    { id: "sejarah", name: "Sejarah" },
    { id: "hukum", name: "Hukum" },
  ];

  const [selected, setSelected] = useState("matematika");

  return (
    <SafeAreaView style={style.containerContent}>
      <CariBuku />
      <View style={{ paddingVertical: 20 }}>
        <KategoriTema
          data={dataKategori}
          selected={selected}
          onSelect={(id) => setSelected(id)}
        />
      </View>

      <View
        style={{ alignItems: "flex-start", width: "100%", paddingLeft: 20 }}
      >
        <Text style={{ fontSize: 24, fontWeight: "600", color: "#305763" }}>
          Buku favorit
        </Text>
      </View>

      <BukuFavorit />

      <View
        style={{ alignItems: "flex-start", width: "100%", paddingLeft: 20 }}
      >
        <Text style={{ fontSize: 24, fontWeight: "600", color: "#305763" }}>
          Novel
        </Text>
      </View>
    </SafeAreaView>
  );
};

export default HomePage;

const style = StyleSheet.create({
  containerContent: {
    flex: 1,
    alignItems: "center",
    backgroundColor: "#f0f0f0f0",
    marginTop: 50,
  },
  titleContainer: {
    backgroundColor: "#5D7BF4",
    width: "100%",
    borderBottomRightRadius: 100,
    justifyContent: "flex-end",
    elevation: 10,
    height: 230,
    paddingBottom: 20,
    paddingLeft: 20,
    paddingRight: 50,
    position: "relative",
  },
  title: {
    color: "#344175",
    fontSize: 30,
    fontWeight: "bold",
  },
});
