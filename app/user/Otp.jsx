import { useEffect, useState } from 'react';
import { useRouter,  } from 'expo-router';
import AsyncStorage from '@react-native-async-storage/async-storage';
import {
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
  Alert,
} from 'react-native';

const Otp = () => {
  const router = useRouter();
  const [otp, setOtp] = useState('');
  const [email, setEmail] = useState('');

  useEffect(() => {
    const fetchEmail = async () => {
      const storedEmail = await AsyncStorage.getItem('resetEmail');
      if (!storedEmail) {
        Alert.alert('Error', 'Email tidak ditemukan. Silakan mulai dari halaman registrasi.');
        router.replace('/user/FirstScreen');
        return;
      }
      setEmail(storedEmail);
    };
    fetchEmail();
  }, [router]);

  const handleVerify = async () => {
    if (otp.length !== 6) {
      Alert.alert('Error', 'Masukkan 6 digit kode OTP');
      return;
    }

    try {
      const response = await fetch('https://267e74522d5a.ngrok-free.app/auth/verify-token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, token: otp }),
      });

      if (response.ok) {
        const data = await response.json();
        if (data.token) {
          await AsyncStorage.setItem('token', data.token);

          try {
            const userResponse = await fetch('https://267e74522d5a.ngrok-free.app/auth/users/', {
              method: 'GET',
              headers: {
                'Authorization': `Bearer ${data.token}`,
                'Content-Type': 'application/json',
              },
            });

            if (userResponse.ok) {
              const userData = await userResponse.json();
              const realname = Array.isArray(userData) ? userData[0]?.realname : userData?.realname;
              if (realname) {
                await AsyncStorage.setItem('realname', realname);
              }
            } else {
              const errorText = await userResponse.text();
              console.log('User API error:', userResponse.status, errorText);
            }
          } catch (error) {
            console.log('Error fetching user data:', error);
          }
        }

        Alert.alert('Success', 'OTP berhasil diverifikasi');
        router.push('/page/HomePage');
      } else {
        const errorText = await response.text();
        Alert.alert('Error', `Verifikasi OTP gagal: ${errorText}`);
      }
    } catch (_error) {
      Alert.alert('Error', 'Terjadi kesalahan jaringan');
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.titleContainer}>
        <Text style={styles.title}>Verifikasi OTP</Text>
        <Text style={{ marginLeft: 20, color: '#BCBCBC', fontSize: 16 }}>
          Masukkan kode OTP yang dikirim ke email Anda
        </Text>
      </View>
      <View style={styles.inputContainer}>
        <Text style={styles.label}>Kode OTP</Text>
        <TextInput
          style={styles.textInput}
          placeholder="6-digit OTP"
          value={otp}
          onChangeText={setOtp}
          keyboardType="numeric"
          maxLength={6}
        />
        <TouchableOpacity style={styles.button} onPress={handleVerify}>
          <Text style={styles.buttonText}>Verifikasi</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f0f0f0',
  },
  titleContainer: {
    backgroundColor: '#5D7BF4',
    height: 286,
    width: '100%',
    borderBottomRightRadius: 100,
    justifyContent: 'center',
    elevation: 10,
  },
  title: {
    color: '#344175',
    fontSize: 40,
    fontWeight: 'bold',
    marginLeft: 20,
  },
  inputContainer: {
    flex: 1,
    width: '100%',
    paddingHorizontal: 20,
    justifyContent: 'center',
  },
  label: {
    fontSize: 15,
    color: '#717171',
    marginBottom: 10,
  },
  textInput: {
    height: 50,
    width: '100%',
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 30,
    paddingHorizontal: 15,
    backgroundColor: '#fff',
    fontSize: 16,
    textAlign: 'center',
  },
  button: {
    backgroundColor: '#5D7BF4',
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 30,
    alignItems: 'center',
    marginTop: 20,
    elevation: 3,
  },
  buttonText: {
    color: '#f0f0f0',
    fontSize: 20,
    fontWeight: 'bold',
  },
});

export default Otp;