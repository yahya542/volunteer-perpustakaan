import React, { useState } from 'react';
import { View, Text, Image, TouchableOpacity, StyleSheet } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import { Ionicons } from '@expo/vector-icons';

const ImageUploader = () => {
  const [profileImage, setProfileImage] = useState(null);
  const [regularImage, setRegularImage] = useState(null);

  const pickProfileImage = async () => {
    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      quality: 1,
    });

    if (!result.canceled) {
      setProfileImage(result.assets[0].uri);
      uploadToDatabase(result.assets[0], 'profile');
    }
  };

  const pickRegularImage = async () => {
    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      quality: 1,
    });

    if (!result.canceled) {
      setRegularImage(result.assets[0].uri);
      uploadToDatabase(result.assets[0], 'regular');
    }
  };

  const uploadToDatabase = async (imageAsset, type) => {
    const formData = new FormData();
    formData.append('file', {
      uri: imageAsset.uri,
      name: `${type}-image.jpg`,
      type: 'image/jpeg',
    });

    try {
      const response = await fetch(`https://your-api.com/upload?type=${type}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        body: formData,
      });

      const data = await response.json();
      console.log(`${type} image uploaded:`, data);
    } catch (error) {
      console.error(`Upload failed for ${type} image:`, error);
    }
  };

  return (
    <View style={styles.container}>
      <View>
        <Text style={styles.label}>Foto Profil</Text>
          <TouchableOpacity style={styles.imageBox} onPress={pickProfileImage}>
            {profileImage ? (
              <Image source={{ uri: profileImage }} style={styles.image} />
            ) : (
              {/* <Text>Pilih Foto Profil</Text> */},
              <Ionicons name="add-circle" size={40} color="white" />
            )}
          </TouchableOpacity>
      </View>

      <View>
        <Text style={styles.label}>Gambar KTP</Text>
          <TouchableOpacity style={styles.imageBox} onPress={pickRegularImage}>
            {regularImage ? (
              <Image source={{ uri: regularImage }} style={styles.image} />
            ) : (
              {/* <Text>Pilih Gambar</Text> */},
              <Ionicons name="add-circle" size={40} color="white" />
            )}
          </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    gap: 20,
    alignItems: 'center',
    marginTop: 20,
    flexDirection: 'row',
  },
  label: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
  },
  imageBox: {
    width: 70,
    height: 70,
    borderRadius: 10,
    backgroundColor: '#38afdbff',
    justifyContent: 'center',
    alignItems: 'center',
  },
  image: {
    width: 120,
    height: 120,
    borderRadius: 10,
  },
});

export default ImageUploader;