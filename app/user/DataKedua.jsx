import { useRouter } from "expo-router";
import { useState, useEffect } from "react";
import AsyncStorage from '@react-native-async-storage/async-storage';
import {
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
  Alert,
} from "react-native";

const DataKedua = () => {
  const router = useRouter();
  const [nama, setNama] = useState('');
  const [tempatLahir, setTempatLahir] = useState('');
  const [tanggalLahir, setTanggalLahir] = useState('');
  const [alamat, setAlamat] = useState('');
  const [institusi, setInstitusi] = useState('');
  const [tipeKeanggotaan, setTipeKeanggotaan] = useState(null);
  const [jenisKelamin, setJenisKelamin] = useState('');
  const [showDropdown, setShowDropdown] = useState(false);
  const [showMembershipDropdown, setShowMembershipDropdown] = useState(false);
  const [nomorTelepon, setNomorTelepon] = useState('');

  const genderOptions = [
    { label: 'Laki-laki', value: 'L' },
    { label: 'Perempuan', value: 'P' },
  ];

  const membershipOptions = [
    { label: '1 - Mahasiswa', value: 'Mahasiswa' },
    { label: '2 - Pelajar', value: 'Pelajar' },
    { label: '3 - Umum', value: 'Umum' },
    { label: '4 - Lainnya', value: 'Lainnya' },
    { label: '5 - Profesional', value: 'Profesional' },
  ];

  useEffect(() => {
    const loadData = async () => {
      try {
        const data = await AsyncStorage.getItem('userData1');
        if (data) {
          const parsed = JSON.parse(data);
          setNama(parsed.nama || '');
          setTempatLahir(parsed.tempatLahir || '');
          setTanggalLahir(parsed.tanggalLahir || '');
          setAlamat(parsed.alamat || '');
        }
      } catch (error) {
        console.error('Error loading data:', error);
      }
    };
    loadData();
  }, []);

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
            Institusi
          </Text>
          <TextInput
            placeholder="Institusi"
            style={style.textInput}
            value={institusi}
            onChangeText={setInstitusi}
          ></TextInput>
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Tipe Keanggotaan
          </Text>
          <TouchableOpacity
            style={style.dropdown}
            onPress={() => setShowMembershipDropdown(!showMembershipDropdown)}
          >
            <Text style={style.dropdownText}>
              {tipeKeanggotaan ? membershipOptions.find(opt => opt.value === tipeKeanggotaan)?.label : 'Pilih Tipe Keanggotaan'}
            </Text>
          </TouchableOpacity>
          {showMembershipDropdown && (
            <View style={style.dropdownList}>
              {membershipOptions.map((option) => (
                <TouchableOpacity
                  key={option.value}
                  style={style.dropdownItem}
                  onPress={() => {
                    setTipeKeanggotaan(option.value);
                    setShowMembershipDropdown(false);
                  }}
                >
                  <Text style={style.dropdownItemText}>{option.label}</Text>
                </TouchableOpacity>
              ))}
            </View>
          )}
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Jenis Kelamin
          </Text>
          <TouchableOpacity
            style={style.dropdown}
            onPress={() => setShowDropdown(!showDropdown)}
          >
            <Text style={style.dropdownText}>
              {jenisKelamin ? genderOptions.find(opt => opt.value === jenisKelamin)?.label : 'Pilih Jenis Kelamin'}
            </Text>
          </TouchableOpacity>
          {showDropdown && (
            <View style={style.dropdownList}>
              {genderOptions.map((option) => (
                <TouchableOpacity
                  key={option.value}
                  style={style.dropdownItem}
                  onPress={() => {
                    setJenisKelamin(option.value);
                    setShowDropdown(false);
                  }}
                >
                  <Text style={style.dropdownItemText}>{option.label}</Text>
                </TouchableOpacity>
              ))}
            </View>
          )}
        </View>
        <View>
          <Text style={{ fontSize: 15, color: "#717171", right: -20 }}>
            Nomor Telepon WA
          </Text>
            <TextInput
              placeholder="Nomor Telepon WA"
              style={style.textInput}
              value={nomorTelepon}
              onChangeText={setNomorTelepon}
            ></TextInput>
        </View>
        <TouchableOpacity
          style={style.button}
          onPress={() => {
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
            if (!alamat.trim()) {
              Alert.alert('Error', 'Alamat Sesuai KTP harus diisi');
              return;
            }
            if (!institusi.trim()) {
              Alert.alert('Error', 'Institusi harus diisi');
              return;
            }
            if (!tipeKeanggotaan) {
              Alert.alert('Error', 'Tipe Keanggotaan harus dipilih');
              return;
            }
            if (!jenisKelamin.trim()) {
              Alert.alert('Error', 'Jenis Kelamin harus dipilih');
              return;
            }
            if (!nomorTelepon.trim()) {
              Alert.alert('Error', 'Nomor Telepon WA harus diisi');
              return;
            }
            const userData = {
              nama,
              tempatLahir,
              tanggalLahir,
              alamat,
              institusi,
              tipeKeanggotaan,
              jenisKelamin,
              nomorTelepon,
            };
            router.push(`/user/register?data=${encodeURIComponent(JSON.stringify(userData))}`);
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

export default DataKedua;

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
  dropdown: {
    height: 50,
    width: 330,
    borderColor: "#ccc",
    borderWidth: 1,
    borderRadius: 30,
    paddingHorizontal: 15,
    backgroundColor: "#fff",
    justifyContent: 'center',
  },
  dropdownText: {
    fontSize: 16,
    color: "#000",
  },
  dropdownList: {
    width: 330,
    backgroundColor: "#fff",
    borderColor: "#ccc",
    borderWidth: 1,
    borderRadius: 10,
    marginTop: 5,
  },
  dropdownItem: {
    padding: 15,
    borderBottomWidth: 1,
    borderBottomColor: "#eee",
  },
  dropdownItemText: {
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
    right: 30, top: 15,
  }
});
