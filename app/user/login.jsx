import React, { useState } from "react";
import { useRouter } from 'expo-router';
import AsyncStorage from '@react-native-async-storage/async-storage';
import {
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
  Alert,
} from "react-native";
import Ionicons from "@expo/vector-icons/Ionicons";

const Login = () => {
  const router = useRouter();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);

  const handleLogin = async () => {
    try {
      console.log('Attempting login with NIK:', username, 'Password:', password);
      const response = await fetch('https://0b8763b66148.ngrok-free.app/auth/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      console.log('Response status:', response.status);
      const data = await response.json();
      console.log('Response data:', data);

      if (response.ok) {
        const token = data.access_token || data.token;
        if (token) {
          await AsyncStorage.setItem('token', token);
          await AsyncStorage.setItem('username', username);

          // ✅ Ambil nama user dari endpoint /auth/users/
          try {
            const memberResponse = await fetch('https://0b8763b66148.ngrok-free.app/auth/users/', {
              method: 'GET',
              headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json',
              },
            });

            console.log('Member API response status:', memberResponse.status);
            const memberData = await memberResponse.json();
            console.log('Member API response JSON:', memberData);

            // ✅ Cocokkan berdasarkan username (NIK) dengan user_id
            const currentUser = memberData.find(m => String(m.username) === String(username));

            if (currentUser?.realname) {
              await AsyncStorage.setItem('realname', currentUser.realname);
              console.log('Stored realname:', currentUser.realname);
            } else {
              console.warn('Nama user tidak ditemukan dalam response');
            }
          } catch (error) {
            console.log('Error fetching member data:', error);
          }
        }

        Alert.alert('Success', 'Login successful');
        router.push('/page/HomePage');
      } else {
        Alert.alert('Error', data.message || 'Login failed');
      }
    } catch (error) {
      console.log('Network error:', error);
      Alert.alert('Error', 'Network error');
    }
  };

  return (
    <View style={style.containerContent}>
      <View style={{ justifyContent: "flex-start", width: "100%" }}>
        <View style={style.titleContainer}>
          <Text style={style.title}>Welcome Back</Text>
          <Text style={{ marginLeft: 20, color: "#BCBCBC", fontSize: 16 }}>
            Sign In Your Account
          </Text>
        </View>
      </View>

      <View style={{ flex: 1, gap: 10 }}>
        <View style={{ marginTop: 20 }}>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>NIK</Text>
          <TextInput
            placeholder="Masukkan NIK"
            value={username}
            onChangeText={setUsername}
            style={style.textInput}
          />
        </View>

        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>Password</Text>
          <View style={{ position: "relative" }}>
            <TextInput
              placeholder="Password"
              value={password}
              onChangeText={setPassword}
              secureTextEntry={!showPassword}
              style={style.textInput}
            />
            <TouchableOpacity
              onPress={() => setShowPassword(!showPassword)}
              style={style.icons}
            >
              <Ionicons
                name={showPassword ? "eye-outline" : "eye-off-outline"}
                size={24}
                color="black"
              />
            </TouchableOpacity>
          </View>
        </View>

        <TouchableOpacity style={style.button} onPress={handleLogin}>
          <Text style={{ color: "#f0f0f0", fontSize: 20, fontWeight: "bold" }}>
            Sign In
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default Login;

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
});