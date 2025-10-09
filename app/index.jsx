import { Image, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import { useRouter } from "expo-router";

const FirstScreen = () => {
  const router = useRouter()

  return (
    <View style={styles.container}>
      <View style={{ flex: 1, marginTop: 120, backgroundColor: "#f0f0f0f0" }}>
        <Image
          source={require("../assets/images/undraw.png")}
          style={{ width: 300, height: 300 }}
        />
      </View>
      <View style={styles.containerButton}>
        <TouchableOpacity style={styles.buttonSignIn} onPress={() => router.push('./user/login')}>
          <Text style={styles.textSignIn}>Sign In</Text>
        </TouchableOpacity>
        <Text style={{ fontSize: 20, fontWeight: "bold", color: "#717171" }}>
          Already have an account
        </Text>
        <TouchableOpacity activeOpacity={0.7} style={styles.buttonSignUp} onPress={() => router.push('/user/DataPertama')}>
          <Text style={styles.textSignUp}>Create Account</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default FirstScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#f0f0f0f0",
  },
  containerButton: { flex: 1, alignItems: "center", gap: 30 },
  buttonSignIn: {
    width: 330,
    height: 61,
    backgroundColor: "#21D54D",
    borderRadius: 30,
    justifyContent: "center",
  },
  textSignIn: {
    textAlign: "center",
    fontSize: 20,
    fontWeight: "bold",
    color: "#f0f0f0",
    elevation: 5,
  },
  buttonSignUp: {
    width: 330,
    height: 61,
    backgroundColor: "#80FF9F",
    borderRadius: 30,
    justifyContent: "center",
  },
  textSignUp: {
    textAlign: "center",
    fontSize: 20,
    fontWeight: "bold",
    color: "#21D54D",
    elevation: 5,
  },
});
