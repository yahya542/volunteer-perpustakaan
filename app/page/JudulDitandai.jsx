import { StyleSheet, Text, View } from "react-native";
import ComponentJudulDitandai from "../../components/judul-ditandai/ComponentJudulDitandai";

const PinjamanTerkini = () => {
  return (
    <View style={style.containerContent}>
      <View style={{ justifyContent: "flex-start", width: "100%" }}>
        <View style={style.titleContainer}>
          <Text style={style.title}>Judul</Text>
          <Text style={style.title}>Tertandai</Text>
        </View>
      </View>
      {/* Bawah */}
        <ComponentJudulDitandai/>
    </View>
  );
};

export default PinjamanTerkini;

const style = StyleSheet.create({
  containerContent: {
    flex: 1,
    alignItems: "center",
    backgroundColor: "#f0f0f0f0",
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
