import { StyleSheet, Text, View } from "react-native";
import ComponentAkunSaya from "../../components/akun-saya/ComponentAkunSaya";

const AkunSaya = () => {
  return (
    <View style={style.containerContent}>
      <View style={{ justifyContent: "flex-start", width: "100%" }}>
        <View style={style.titleContainer}>
          <Text style={style.title}>Akun Saya</Text>
        </View>
      </View>
      {/* Bawah */}
      <View style={{ width: "90%", backgroundColor: "#ffffff", height: "50%", marginTop: 20, boxShadow:"3px 4px 24px -1px rgba(112, 112, 112, 0.62);" }}>
        <ComponentAkunSaya />
      </View>
    </View>
  );
};

export default AkunSaya;
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










