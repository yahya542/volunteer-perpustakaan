import { Text, TextInput, TouchableOpacity, View, } from "react-native";

const register = () => {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#f0f0f0f0",
      }}
    >
      <View style={{ justifyContent: "flex-start", width: "100%" }}>
        <View
          style={{
            backgroundColor: "#5D7BF4",
            height: 286,
            width: "100%",
            borderBottomRightRadius: 100,
            justifyContent: "center",
            elevation: 10,
          }}
        >
          <Text
            style={{
              color: "#344175",
              fontSize: 40,
              fontWeight: "bold",
              marginLeft: 20,
            }}
          >
            Create Account
          </Text>
          <Text style={{ marginLeft: 20, color: "#BCBCBC", fontSize: 16 }}>
            Sign Up Your Account
          </Text>
        </View>
      </View>
      {/* Bawah */}
      <View
        style={{
          flex: 1,
          gap: 20,
        }}
      >
        <View>
          <View
            style={{
              height: 70,
              width: 70,
              backgroundColor: "#D9D9D9",
              borderRadius: 100,
              marginTop: 30,
            }}
          ></View>
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            NIK
          </Text>
          <TextInput
            placeholder="Masukkan NIK"
            style={{
              height: 50,
              width: 330,
              borderColor: "#ccc",
              borderWidth: 1,
              borderRadius: 30,
              paddingHorizontal: 15,
              backgroundColor: "#fff",
              fontSize: 16,
            }}
          ></TextInput>
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Nama Lengkap
          </Text>
          <TextInput
            placeholder="Nama Lengkap"
            style={{
              height: 50,
              width: 330,
              borderColor: "#ccc",
              borderWidth: 1,
              borderRadius: 30,
              paddingHorizontal: 15,
              backgroundColor: "#fff",
              fontSize: 16,
            }}
          ></TextInput>
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Email
          </Text>
          <TextInput
            placeholder="Email"
            style={{
              height: 50,
              width: 330,
              borderColor: "#ccc",
              borderWidth: 1,
              borderRadius: 30,
              paddingHorizontal: 15,
              backgroundColor: "#fff",
              fontSize: 16,
            }}
          ></TextInput>
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Password
          </Text>
          <TextInput
            placeholder="Password"
            secureTextEntry={true}
            style={{
              height: 50,
              width: 330,
              borderColor: "#ccc",
              borderWidth: 1,
              borderRadius: 30,
              paddingHorizontal: 15,
              backgroundColor: "#fff",
              fontSize: 16,
            }}
          ></TextInput>
        </View>
        <TouchableOpacity
          style={{
            backgroundColor: "#5D7BF4",
            paddingVertical: 14,
            paddingHorizontal: 24,
            borderRadius: 30,
            alignItems: "center",
            marginTop: 20,
            elevation: 3,
          }}
        >
          <Text style={{ color: "#f0f0f0", fontSize: 20, fontWeight: "bold" }}>
            Sign Up
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default register;
