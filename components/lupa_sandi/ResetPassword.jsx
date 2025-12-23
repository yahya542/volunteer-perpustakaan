import AsyncStorage from "@react-native-async-storage/async-storage";
import { useRouter } from "expo-router";
import { useEffect, useState } from "react";
import {
  Alert,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from "react-native";

const ResetPassword = () => {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [token, setToken] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  useEffect(() => {
    const loadData = async () => {
      const storedEmail = await AsyncStorage.getItem("resetEmail");
      const storedToken = await AsyncStorage.getItem("token");
      if (!storedEmail || !storedToken) {
        Alert.alert("Error", "Data tidak lengkap. Silakan mulai ulang.");
        router.replace("/user/Login");
        return;
      }
      setEmail(storedEmail);
      setToken(storedToken);
    };
    loadData();
  }, [router]);

  const handleResetPassword = async () => {
    if (newPassword !== confirmPassword) {
      Alert.alert("Error", "Konfirmasi sandi tidak cocok");
      return;
    }

    try {
      const response = await fetch("https://your-api-url.com/auth/reset-password/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email,
          token,
          new_password: newPassword,
        }),
      });

      const data = await response.json();
      if (response.ok) {
        Alert.alert("Berhasil", "Sandi berhasil diubah. Silakan login.");
        await AsyncStorage.multiRemove(["resetEmail", "token", "otpPurpose"]);
        router.replace("/user/Login");
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
      <View style={styles.header}>
        <Text style={styles.title}>Reset Password</Text>
        <Text style={styles.subtitle}>Masukkan sandi baru Anda</Text>
      </View>

      <View style={styles.form}>
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
        <TouchableOpacity style={styles.button} onPress={handleResetPassword}>
          <Text style={styles.buttonText}>Ubah Sandi</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default ResetPassword;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f0f0f0",
  },
  header: {
    backgroundColor: "#5D7BF4",
    height: 200,
    borderBottomRightRadius: 100,
    justifyContent: "center",
    paddingLeft: 20,
  },
  title: {
    color: "#344175",
    fontSize: 32,
    fontWeight: "bold",
  },
  subtitle: {
    color: "#BCBCBC",
    fontSize: 16,
    marginTop: 8,
  },
  form: {
    padding: 30,
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
    backgroundColor: "#fff",
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