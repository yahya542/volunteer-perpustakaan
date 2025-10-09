import { useRouter } from "expo-router";
import { useState } from "react";
import AsyncStorage from '@react-native-async-storage/async-storage';
import {
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
  Alert,
} from "react-native";

const DataPertama = () => {
  const router = useRouter();
  const [nama, setNama] = useState("");
  const [tempatLahir, setTempatLahir] = useState("");
  const [tanggalLahir, setTanggalLahir] = useState("");
  const [alamat, setAlamat] = useState("");

  return (
    <View style={style.containerContent}>
      <View style={{ justifyContent: "flex-start", width: "100%" }}>
        <View style={style.titleContainer}>
          <Text style={style.title}>Create Account</Text>
          <Text style={{ marginLeft: 20, color: "#BCBCBC", fontSize: 16 }}>
            Lengkapi Data Diri
          </Text>
        </View>
      </View>
      {/* Bawah */}
      <View style={{ flex: 1, gap: 10 }}>
        <View style={{ flexDirection: "row", alignItems: "center", gap: 20 }}>
          {/* <View style={style.inputProfil}></View> */}
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Nama
          </Text>
          <TextInput
            placeholder="Masukkan Nama"
            style={style.textInput}
            value={nama}
            onChangeText={setNama}
          ></TextInput>
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Tempat Lahir
          </Text>
          <TextInput
            placeholder="Tempat Lahir"
            style={style.textInput}
            value={tempatLahir}
            onChangeText={setTempatLahir}
          ></TextInput>
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Tanggal Lahir
          </Text>
          <TextInput
            placeholder="Tanggal Lahir (YYYY-MM-DD)"
            style={style.textInput}
            value={tanggalLahir}
            onChangeText={setTanggalLahir}
          ></TextInput>
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Alamat Sesuai KTP
          </Text>
          <TextInput
            placeholder="Alamat Sesuai KTP"
            style={style.textInput}
            value={alamat}
            onChangeText={setAlamat}
          ></TextInput>
        </View>
        <TouchableOpacity
          style={style.button}
          onPress={async () => {
            if (!nama.trim()) {
              Alert.alert('Error', 'Nama harus diisi');
              return;
            }
            if (!tempatLahir.trim()) {
              Alert.alert('Error', 'Tempat Lahir harus diisi');
              return;
            }
            if (!tanggalLahir.trim()) {
              Alert.alert('Error', 'Tanggal Lahir harus diisi');
              return;
            }
            const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
            if (!dateRegex.test(tanggalLahir)) {
              Alert.alert('Error', 'Tanggal Lahir harus dalam format YYYY-MM-DD (tahun-bulan-hari)');
              return;
            }
            if (!alamat.trim()) {
              Alert.alert('Error', 'Alamat Sesuai KTP harus diisi');
              return;
            }
            await AsyncStorage.setItem('userData1', JSON.stringify({nama, tempatLahir, tanggalLahir, alamat}));
            router.push('/user/DataKedua');
          }}
        >
          <Text style={{ color: "#f0f0f0", fontSize: 20, fontWeight: "bold" }}>
            Selanjutnya
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default DataPertama;

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
});
