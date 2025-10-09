import { useState } from 'react';
import { useRouter, useLocalSearchParams } from 'expo-router';
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
  const { token } = useLocalSearchParams();
  const [email, setEmail] = useState('');
  const [otp, setOtp] = useState('');

  const handleVerify = async () => {
    if (!email.trim()) {
      Alert.alert('Error', 'Email harus diisi');
      return;
    }
    if (otp.length !== 6) {
      Alert.alert('Error', 'Please enter a 6-digit OTP');
      return;
    }

    console.log('Token received:', token);
    console.log('Request body:', { email, token: otp });

    try {
      const response = await fetch('https://0b8763b66148.ngrok-free.app/auth/verify-token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, token: otp }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Verification response:', data);
        if (data.token) {
          await AsyncStorage.setItem('token', data.token);
          // Fetch user data and store realname
          try {
            const userResponse = await fetch('https://0b8763b66148.ngrok-free.app/auth/users/', {
              method: 'GET',
              headers: {
                'Authorization': `Bearer ${data.token}`,
                'Content-Type': 'application/json',
              },
            });
            console.log('User API response status:', userResponse.status);
            if (userResponse.ok) {
              const userData = await userResponse.json();
              console.log('User data from API:', userData);
              const realname = Array.isArray(userData) ? userData[0]?.realname : userData?.realname;
              console.log('Extracted realname:', realname);
              if (realname) {
                await AsyncStorage.setItem('realname', realname);
              }
            } else {
              const errorText = await userResponse.text();
              console.log('User API error:', userResponse.status, errorText);
            }
          } catch (error) {
            console.log('Error fetching user data on verification:', error);
          }
        }
        Alert.alert('Success', 'OTP verified successfully');
        router.push('/page/HomePage');
      } else {
        const errorText = await response.text();
        console.log('Response status:', response.status);
        console.log('Response text:', errorText);
        Alert.alert('Error', `OTP verification failed: ${errorText}`);
      }
    } catch (_error) {
      Alert.alert('Error', 'Network error');
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.titleContainer}>
        <Text style={styles.title}>Verify OTP</Text>
        <Text style={{ marginLeft: 20, color: '#BCBCBC', fontSize: 16 }}>
          Enter the OTP sent to your device
        </Text>
      </View>
      <View style={styles.inputContainer}>
        <Text style={styles.label}>Email</Text>
        <TextInput
          style={styles.textInput}
          placeholder="Enter your email"
          value={email}
          onChangeText={setEmail}
          keyboardType="email-address"
        />
        <Text style={styles.label}>OTP Code</Text>
        <TextInput
          style={styles.textInput}
          placeholder="Enter 6-digit OTP"
          value={otp}
          onChangeText={setOtp}
          keyboardType="numeric"
          maxLength={6}
        />
        <TouchableOpacity style={styles.button} onPress={handleVerify}>
          <Text style={styles.buttonText}>Verify OTP</Text>
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