import React, { useState } from 'react';
import { View, TextInput, StyleSheet } from 'react-native';
import { useRouter } from 'expo-router';

const CariBuku = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const router = useRouter();

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Cari buku..."
        value={searchTerm}
        onChangeText={setSearchTerm}
        onSubmitEditing={() => router.push('/page/CariJudulBuku')}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 16,
    height:70
  },
  input: {
    width: 328,
    height: 49,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 16,
    paddingHorizontal: 8,
    borderRadius: 20,
    border: "nome",
    paddingLeft: 20,
  },
  list: {
    flex: 1,
  },
  bookItem: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  author: {
    fontSize: 14,
    color: '#666',
  },
});

export default CariBuku;