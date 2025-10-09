import { Text, View } from "react-native";
import React, { useState, useEffect } from 'react';
import { getCurrentUser } from '../utils/getCurrentUser'; // pastikan path sesuai

const ComponentAkunSaya = () => {
  const [membership, setMembership] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchMembership();
  }, []);

  const fetchMembership = async () => {
    try {
      const user = await getCurrentUser();
      if (!user) {
        setLoading(false);
        return;
      }

      const response = await fetch('https://0b8763b66148.ngrok-free.app/user/members/', {
        headers: {
          'Authorization': `Token ${user.token}`,
        },
      });

      const text = await response.text();
      console.log('Response status:', response.status);
      console.log('Response text:', text);

      if (response.ok) {
        const data = JSON.parse(text);

        const currentUser = data.find(member => member.member_id === user.username);

        if (currentUser) {
          setMembership({
            namaAnggota: currentUser.member_name,
            surel: currentUser.member_email,
            tanggalRegistrasi: currentUser.register_date,
            institusi: currentUser.inst_name,
            idAnggota: currentUser.member_id,
            tipeKeanggotaan: currentUser.member_type_id,
            berlakuHingga: currentUser.expire_date,
          });
        } else {
          console.warn('User tidak ditemukan dalam response');
        }
      } else {
        console.error('Server error:', text);
      }
    } catch (error) {
      console.error('Error fetching membership details:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={{ alignItems: "flex-start", flex: 1, width: "auto", padding: 20, gap: 10 }}>
      <Text style={{ fontSize: 24, fontWeight: "bold" }}>Detail Keanggotaan</Text>

      {loading ? (
        <Text>Memuat data...</Text>
      ) : (
        <>
          <View style={{ flexDirection: "row", gap: 5 }}>
            <Text style={{ fontWeight: "bold" }}>Nama Anggota : </Text>
            <Text>{membership.namaAnggota || '-'}</Text>
          </View>
          <View style={{ flexDirection: "row", gap: 5 }}>
            <Text style={{ fontWeight: "bold" }}>Surel : </Text>
            <Text>{membership.surel || '-'}</Text>
          </View>
          <View style={{ flexDirection: "row", gap: 5 }}>
            <Text style={{ fontWeight: "bold" }}>Tanggal Registrasi : </Text>
            <Text>{membership.tanggalRegistrasi ? new Date(membership.tanggalRegistrasi).toLocaleDateString() : '-'}</Text>
          </View>
          <View style={{ flexDirection: "row", gap: 5 }}>
            <Text style={{ fontWeight: "bold" }}>Institusi : </Text>
            <Text>{membership.institusi || '-'}</Text>
          </View>
          <View style={{ flexDirection: "row", gap: 5 }}>
            <Text style={{ fontWeight: "bold" }}>ID Anggota : </Text>
            <Text>{membership.idAnggota || '-'}</Text>
          </View>
          <View style={{ flexDirection: "row", gap: 5 }}>
            <Text style={{ fontWeight: "bold" }}>Tipe Keanggotaan : </Text>
            <Text>{membership.tipeKeanggotaan || '-'}</Text>
          </View>
          <View style={{ flexDirection: "row", gap: 5 }}>
            <Text style={{ fontWeight: "bold" }}>Berlaku Hingga : </Text>
            <Text>{membership.berlakuHingga ? new Date(membership.berlakuHingga).toLocaleDateString() : '-'}</Text>
          </View>
        </>
      )}
    </View>
  );
};

export default ComponentAkunSaya;