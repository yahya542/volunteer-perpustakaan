import AsyncStorage from "@react-native-async-storage/async-storage";
import { useRouter } from "expo-router";
import { useState } from "react";
import {
  Alert,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from "react-native";

const LupaSandi = () => {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [isVerified, setIsVerified] = useState(false);
  const [token, setToken] = useState("");

  const handleVerifyEmail = async () => {
    try {
      const response = await fetch(
        "https://your-api-url.com/auth/request-reset/",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email }),
        }
      );

      const data = await response.json();
      if (response.ok && data.token) {
        setToken(data.token);
        setIsVerified(true);
        Alert.alert(
          "Berhasil",
          "Email ditemukan. Silakan masukkan sandi baru."
        );
      } else {
        Alert.alert("Gagal", data.message || "Email tidak ditemukan");
      }
    } catch (error) {
      console.error("Verifikasi error:", error);
      Alert.alert("Error", "Terjadi kesalahan saat verifikasi email");
    }
  };

  const handleResetPassword = async () => {
    if (newPassword !== confirmPassword) {
      Alert.alert("Error", "Konfirmasi sandi tidak cocok");
      return;
    }

    try {
      const response = await fetch(
        "https://your-api-url.com/auth/reset-password/",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            email,
            token,
            new_password: newPassword,
          }),
        }
      );

      const data = await response.json();
      if (response.ok) {
        await AsyncStorage.setItem("token", token);
        await AsyncStorage.setItem("email", email);
        await AsyncStorage.setItem("password", newPassword);

        Alert.alert(
          "Berhasil",
          "Sandi berhasil diubah. Silakan login kembali."
        );
        router.push("/page/user/Login"); // ⬅️ sesuaikan dengan path login kamu
      } else {
        Alert.alert("Gagal", data.message || "Gagal mengubah sandi");
      }
    } catch (error) {
      console.error("Reset error:", error);
      Alert.alert("Error", "Terjadi kesalahan saat mengubah sandi");
    }
  };

  return (
    <View style={styles.container}>
      <View style={{ justifyContent: "flex-start", width: "100%" }}>
        <View style={styles.titleContain}>
          <Text style={styles.headerstitle}>Welcome Back</Text>
          <Text style={{ marginLeft: 20, color: "#BCBCBC", fontSize: 16 }}>
            Sign In Your Account
          </Text>
        </View>
      </View>

      <View style={{ padding: 30}}>
        {!isVerified ? (
          <>
            <Text style={styles.label}>Masukkan Email Anda:</Text>
            <TextInput
              style={styles.input}
              placeholder="Email"
              keyboardType="email-address"
              value={email}
              onChangeText={setEmail}
            />
            <TouchableOpacity style={styles.button} onPress={handleVerifyEmail}>
              <Text style={styles.buttonText}>Kirim OTP / Token</Text>
            </TouchableOpacity>
          </>
        ) : (
          <>
            <Text style={styles.label}>Sandi Baru:</Text>
            <TextInput
              style={styles.input}
              placeholder="Sandi baru"
              secureTextEntry
              value={newPassword}
              onChangeText={setNewPassword}
            />
            <Text style={styles.label}>Konfirmasi Sandi:</Text>
            <TextInput
              style={styles.input}
              placeholder="Ulangi sandi"
              secureTextEntry
              value={confirmPassword}
              onChangeText={setConfirmPassword}
            />
            <TouchableOpacity
              style={styles.button}
              onPress={handleResetPassword}
            >
              <Text style={styles.buttonText}>Ubah Sandi</Text>
            </TouchableOpacity>
          </>
        )}
      </View>
    </View>
  );
};

export default LupaSandi;

const styles = StyleSheet.create({
  titleContain: {
    backgroundColor: "#5D7BF4",
    height: 286,
    width: "100%",
    borderBottomRightRadius: 100,
    justifyContent: "center",
    elevation: 10,
  },
  headerstitle: {
    color: "#344175",
    fontSize: 40,
    fontWeight: "bold",
    marginLeft: 20,
  },
  container: {
    backgroundColor: "#ffbcbcff",
    flex: 1,
    justifyContent: "flex-start",
  },
  label: {
    fontSize: 16,
    marginBottom: 8,
  },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 10,
    marginBottom: 20,
  },
  button: {
    backgroundColor: "#5D7BF4",
    padding: 14,
    borderRadius: 8,
    alignItems: "center",
  },
  buttonText: {
    color: "#fff",
    fontWeight: "bold",
  },
});
