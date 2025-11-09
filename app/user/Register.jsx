import Ionicons from "@expo/vector-icons/Ionicons";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { useLocalSearchParams, useRouter } from "expo-router";
import { useEffect, useState } from "react";
import {
  Alert,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from "react-native";

const Register = () => {
  const router = useRouter();
  const [showPassword, setShowPassword] = useState(false);
  const [nik, setNik] = useState("");
  const [namaLengkap, setNamaLengkap] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const { data } = useLocalSearchParams();

  useEffect(() => {
    if (data) {
      try {
        const parsed = JSON.parse(data);
        setNamaLengkap(parsed.nama || "");
      } catch (error) {
        console.error("Error parsing data:", error);
      }
    }
  }, [data]);

  const handleRegister = async () => {
    if (
      !nik.trim() ||
      !namaLengkap.trim() ||
      !email.trim() ||
      !password.trim() ||
      !confirmPassword.trim()
    ) {
      Alert.alert("Error", "Semua field wajib diisi");
      return;
    }
    if (password !== confirmPassword) {
      setPasswordError("Passwords do not match");
      return;
    } else {
      setPasswordError("");
    }
    if (password.length < 8) {
      Alert.alert("Error", "Password minimal 8 karakter");
      return;
    }

    const previousData = data
      ? (() => {
          try {
            return JSON.parse(data);
          } catch {
            return {};
          }
        })()
      : {};

    const requiredFields = [
      "nama",
      "tempatLahir",
      "tanggalLahir",
      "alamat",
      "institusi",
      "tipeKeanggotaan",
      "jenisKelamin",
      "nomorTelepon",
    ];
    for (const field of requiredFields) {
      if (!previousData[field] || !previousData[field].trim()) {
        Alert.alert("Error", `${field} harus diisi`);
        return;
      }
    }

    const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
    if (!dateRegex.test(previousData.tanggalLahir)) {
      Alert.alert("Error", "Tanggal Lahir harus format YYYY-MM-DD");
      return;
    }

    const fullData = {
      username: nik,
      realname: namaLengkap,
      passwd: password,
      nama: namaLengkap,
      nik: nik,
      tanggal_lahir: previousData.tanggalLahir,
      tipe_keanggotaan: previousData.tipeKeanggotaan,
      jenis_kelamin: previousData.jenisKelamin,
      alamat: previousData.alamat,
      nomor_hp: previousData.nomorTelepon,
      password: password,
      konfirmasi_password: confirmPassword,
      email: email,
      tempat_lahir: previousData.tempatLahir,
      institusi: previousData.institusi,
    };

    try {
      const response = await fetch(
        "https://267e74522d5a.ngrok-free.app/auth/register/",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(fullData),
        }
      );

      console.log("Request data:", fullData);
      console.log("Response status:", response.status);
      const responseText = await response.text();
      console.log("Response text:", responseText);

      let parsedResponse;
      try {
        parsedResponse = JSON.parse(responseText);
      } catch {
        parsedResponse = { token: null };
      }

      if (response.ok) {
        try {
          if (parsedResponse.token) {
            await AsyncStorage.setItem("token", parsedResponse.token);
            // await AsyncStorage.setItem("realname", namaLengkap);
          }
          await AsyncStorage.setItem("username", nik);
          await AsyncStorage.setItem("realname", namaLengkap);
          console.log("Stored username:", nik);
          console.log("Stored realname:", namaLengkap);
        } catch (storageError) {
          console.error("Error saving to AsyncStorage:", storageError);
        }

        Alert.alert("Success", "Registration successful");
        // router.push(`/user/Otp?token=${parsedResponse.token}`);
        await AsyncStorage.setItem("resetEmail", email);
        router.push("/user/Otp");
      } else {
        Alert.alert(
          "Error",
          `Registration failed: ${response.status} - ${responseText}`
        );
      }
    } catch (error) {
      Alert.alert("Error", "Network error");
      console.error("Network error:", error);
    }
  };

  return (
    <View style={style.containerContent}>
      <View style={{ justifyContent: "flex-start", width: "100%" }}>
        <View style={style.titleContainer}>
          <Text style={style.title}>Create Account</Text>
          <Text style={{ marginLeft: 20, color: "#BCBCBC", fontSize: 16 }}>
            Sign Up Your Account
          </Text>
        </View>
      </View>

      <View style={{ flex: 1, gap: 10 }}>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            NIK
          </Text>
          <TextInput
            placeholder="Masukkan NIK"
            style={style.textInput}
            value={nik}
            onChangeText={setNik}
          />
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Nama Lengkap
          </Text>
          <TextInput
            placeholder="Nama Lengkap"
            style={style.textInput}
            value={namaLengkap}
            onChangeText={setNamaLengkap}
          />
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Email
          </Text>
          <TextInput
            placeholder="Email"
            style={style.textInput}
            value={email}
            onChangeText={setEmail}
          />
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Password
          </Text>
          <View style={{ position: "relative" }}>
            <TextInput
              placeholder="Password"
              secureTextEntry={!showPassword}
              style={style.textInput}
              value={password}
              onChangeText={setPassword}
            />
            <TouchableOpacity
              onPress={() => setShowPassword(!showPassword)}
              style={style.icons}
            >
              <Ionicons
                name={showPassword ? "eye-off-outline" : "eye-outline"}
                size={24}
                color="black"
              />
            </TouchableOpacity>
          </View>
          <Text
            style={{
              fontSize: 15,
              color: "#717171",
              right: -20,
              marginTop: 10,
            }}
          >
            Confirm Password
          </Text>
          <View style={{ position: "relative", marginTop: 5 }}>
            <TextInput
              placeholder="Confirm Password"
              secureTextEntry={!showPassword}
              style={style.textInput}
              value={confirmPassword}
              onChangeText={setConfirmPassword}
            />
            <TouchableOpacity
              onPress={() => setShowPassword(!showPassword)}
              style={style.icons}
            >
              <Ionicons
                name={showPassword ? "eye-off-outline" : "eye-outline"}
                size={24}
                color="black"
              />
            </TouchableOpacity>
          </View>
          {passwordError ? (
            <Text style={{ color: "red", fontSize: 14, marginTop: 5 }}>
              {passwordError}
            </Text>
          ) : null}
        </View>

        <TouchableOpacity style={style.button} onPress={handleRegister}>
          <Text style={{ color: "#f0f0f0", fontSize: 20, fontWeight: "bold" }}>
            Sign Up
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default Register;

const style = StyleSheet.create({
  containerContent: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#f0f0f0f0",
  },
  titleContainer: {
    backgroundColor: "#5D7BF4",
    height: 286,
    width: "100%",
    borderBottomRightRadius: 100,
    justifyContent: "center",
    elevation: 10,
  },
  title: {
    color: "#344175",
    fontSize: 40,
    fontWeight: "bold",
    marginLeft: 20,
  },
  inputProfil: {
    height: 70,
    width: 70,
    backgroundColor: "#D9D9D9",
    borderRadius: 100,
    marginTop: 30,
  },
  textInput: {
    height: 50,
    width: 330,
    borderColor: "#ccc",
    borderWidth: 1,
    borderRadius: 30,
    paddingHorizontal: 15,
    backgroundColor: "#fff",
    fontSize: 16,
  },
  button: {
    backgroundColor: "#5D7BF4",
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 30,
    alignItems: "center",
    marginTop: 20,
    elevation: 3,
  },
  icons: {
    position: "absolute",
    right: 30,
    top: 15,
  },
  button_2: {
    backgroundColor: "#5D7BF4",
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 30,
    alignItems: "center",
    marginTop: 20,
    elevation: 3,
  },
});
