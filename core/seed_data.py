"""Data riil PCM Masaran untuk command `seed_pcm`.

Sumber (catat juga di README -> tabel data / sumber / tanggal diambil):
- "Rancangan Profil Pimpinan Cabang Muhammadiyah Masaran" (dokumen PCM)
- "Struktur Pengurus PCM Masaran 2022-2027 (paripurna)" (dokumen PCM)

Hal yang BELUM tersedia dibiarkan kosong (jangan diisi tebakan):
tagline, telepon, email, jumlah anggota ber-KTAM, berita, agenda, URL PDM/PWM.
"""

DATA = {
    "profil": {
        "name": "Pimpinan Cabang Muhammadiyah Masaran",
        "short_name": "PCM Masaran",
        "tagline": "",
        "description": (
            "Pimpinan Cabang Muhammadiyah (PCM) Masaran merupakan salah satu struktur "
            "organisasi Persyarikatan Muhammadiyah pada tingkat kecamatan yang berada di "
            "bawah koordinasi Pimpinan Daerah Muhammadiyah (PDM) Kabupaten Sragen dan "
            "Pimpinan Wilayah Muhammadiyah (PWM) Jawa Tengah. Sebagai organisasi dakwah "
            "Islam yang berlandaskan Al-Qur'an dan As-Sunnah, PCM Masaran menjadi "
            "penggerak berbagai aktivitas dakwah, pendidikan, sosial, kesehatan, ekonomi, "
            "serta pemberdayaan masyarakat di wilayah Kecamatan Masaran."
        ),
        "history": (
            "Muhammadiyah didirikan oleh KH. Ahmad Dahlan pada 18 November 1912 di "
            "Yogyakarta sebagai gerakan Islam yang mengusung semangat tajdid (pembaruan), "
            "pemurnian akidah, serta pembinaan umat melalui pendidikan, pelayanan sosial, "
            "kesehatan, dan dakwah. Semangat tersebut kemudian berkembang ke berbagai "
            "daerah, termasuk Kabupaten Sragen.\n\n"
            "Di Kecamatan Masaran, benih-benih dakwah Muhammadiyah tumbuh melalui aktivitas "
            "para ulama, tokoh masyarakat, dan warga yang peduli pada kemajuan pendidikan "
            "Islam dan kehidupan sosial keagamaan. Pimpinan Cabang Muhammadiyah Masaran "
            "berdiri pada tahun 1932, bersamaan dengan berdirinya group-group (ranting) di "
            "berbagai daerah antara lain Gondang, Sukdono, Sambirejo, Gemolong, "
            "Karangmalang, Kalijambe, dan Sidoharjo. Berdirinya PCM Masaran menjadi "
            "tonggak penting perkembangan Muhammadiyah di wilayah barat Kabupaten Sragen.\n\n"
            "Balai Muhammadiyah Masaran berdiri di atas tanah wakaf keluarga Bapak Hartono. "
            "Di kompleks tersebut berdiri Kantor Sekretariat PCM Masaran, Balai "
            "Muhammadiyah, Masjid Amanah, KB dan TK 'Aisyiyah Masaran 2, serta Rumah "
            "Tahfiz Daarul Arqam Muhammadiyah Masaran."
        ),
        "vision": (
            "Menegakkan dan menjunjung tinggi Agama Islam sehingga terwujud masyarakat "
            "Islam yang sebenar-benarnya"
        ),
        "mission": [
            "Meningkatkan kualitas iman, ibadah, dan akhlak warga cabang.",
            "Mengoptimalkan peran Pimpinan Ranting (PRM) di tingkat kelurahan/desa sebagai garda terdepan.",
            "Mengembangkan Amal Usaha Muhammadiyah (AUM) seperti sekolah, klinik, atau panti asuhan agar bermanfaat luas.",
            "Memperkuat dakwah amar ma'ruf nahi mungkar dan pembaharuan (tajdid).",
            "Menjalin kerja sama yang baik dengan masyarakat dan pemerintah setempat.",
        ],
        "address": (
            "Jl. Kelapa No. 10 RT 30 RW 10, Masaran, Kecamatan Masaran, "
            "Kabupaten Sragen 57282"
        ),
        "phone": "",
        "email": "",
        "logo": "",  # nama file di core/seed_images/, mis. "logo-muhammadiyah.png"
    },

    # Struktur Pengurus Periode Muktamar 48, 2022-2027
    "pimpinan": [
        {"name": "Drs. H. Sutarno, MM", "position": "Penasehat", "period": "2022–2027"},
        {"name": "Ir. H. Suroto", "position": "Penasehat", "period": "2022–2027"},
        {"name": "H. Siyamto Umardani, S. Ag", "position": "Ketua", "period": "2022–2027"},
        {"name": "Giyamto, S. Pd", "position": "Wakil Ketua I", "period": "2022–2027",
         "description": "Koordinator: Majelis Pemberdayaan Masyarakat; Lazismu"},
        {"name": "H. Sumarno, S. Th. I", "position": "Wakil Ketua II", "period": "2022–2027",
         "description": "Koordinator: Lembaga Pembinaan Haji dan Umroh; Lembaga Pembinaan dan Pengawasan Keuangan"},
        {"name": "Parlan Sinung Darsono", "position": "Wakil Ketua III", "period": "2022–2027",
         "description": "Koordinator: Majelis Pembinaan Kader – Sumber Daya Insani; Lembaga Sosial Budaya dan Olah Raga, Pembinaan Angkatan Muda Muhammadiyah dan Ortom"},
        {"name": "H. Suyatno, S. Sos, M. Si", "position": "Wakil Ketua IV", "period": "2022–2027",
         "description": "Koordinator: Majelis Pemberdayaan Wakaf; Majelis Lingkungan Hidup"},
        {"name": "Muhammad Marjuki, S. Pd", "position": "Wakil Ketua V", "period": "2022–2027",
         "description": "Koordinator: Majelis Tarjih, Tajdid, dan Tabligh; Lembaga Pengembangan Cabang Ranting dan Pembinaan Masjid"},
        {"name": "Dr. H. Basuki Agus Suparno, MSI", "position": "Wakil Ketua VI", "period": "2022–2027",
         "description": "Koordinator: Majelis Pustaka dan Informasi; Majelis Hukum, HAM, dan Lembaga Bantuan Hukum"},
        {"name": "Dr. Purwadi, M. Pd", "position": "Wakil Ketua VII", "period": "2022–2027",
         "description": "Koordinator: Majelis Dikdasmen; Lembaga Pengembangan Pesantren Muhammadiyah"},
        {"name": "Dr. H. Suharno, ST. MT", "position": "Wakil Ketua VIII", "period": "2022–2027",
         "description": "Koordinator: Majelis Ekonomi dan Kewirausahaan; Lembaga Hikmah dan Kebijakan Publik"},
        {"name": "Muhammad Effendi, S. Psi", "position": "Sekretaris", "period": "2022–2027"},
        {"name": "Drs. H. Taslim Daryanto, M. Pd", "position": "Wakil Sekretaris", "period": "2022–2027",
         "description": "Koordinator: MPKU dan Pelayanan Sosial"},
        {"name": "Dwi Daryanto, S. Pd. I", "position": "Bendahara", "period": "2022–2027"},
        {"name": "Muslih, S. Pd", "position": "Wakil Bendahara", "period": "2022–2027",
         "description": "Koordinator: Lembaga Resiliensi Bencana"},
    ],

    # 13 Pimpinan Ranting Muhammadiyah (ketua belum tersedia)
    "ranting": [{"name": n} for n in [
        "PRM Masaran", "PRM Krikilan", "PRM Gebang", "PRM Pringanom", "PRM Sepat",
        "PRM Krebet", "PRM Jirapan", "PRM Dawungan", "PRM Karangmalang",
        "PRM Sidodadi", "PRM Kliwonan", "PRM Pilang", "PRM Jati",
    ]],

    "amal_usaha": [
        # --- Pendidikan formal (9 AUM) ---
        {"name": "SMK Muhammadiyah 10 Masaran", "category": "pendidikan",
         "address": "Jl. Raya Sragen–Solo KM 10, RT 25/RW 10, Masaran, Kecamatan Masaran, Kabupaten Sragen 57282",
         "description": "Pendidikan kejuruan yang berorientasi pada penguasaan kompetensi, penguatan karakter Islami, dan kesiapan lulusan memasuki dunia kerja."},
        {"name": "SMA Muhammadiyah 3 Masaran", "category": "pendidikan",
         "address": "Jl. Raya Sragen–Solo KM 10, RT 09/RW 02, Masaran Kulon, Desa Jati, Kecamatan Masaran, Kabupaten Sragen 57282",
         "description": "Pendidikan menengah yang memadukan penguasaan ilmu pengetahuan, pembinaan akhlak, dan pengembangan prestasi."},
        {"name": "SMP Muhammadiyah 2 Masaran", "category": "pendidikan",
         "address": "Jl. Raya Sragen–Solo KM 10, RT 25/RW 10, Masaran, Kecamatan Masaran, Kabupaten Sragen 57282"},
        {"name": "MTs Muhammadiyah 3 Masaran", "category": "pendidikan",
         "address": "Kliwonan RT 13, Desa Kliwonan, Kecamatan Masaran, Kabupaten Sragen 57282"},
        {"name": "Pondok Pesantren Tahfiz Al-Qur'an (PPTQ) Darul Hikmah Muhammadiyah Masaran", "category": "pendidikan",
         "address": "Gondang RT 22/RW 07, Desa Jirapan, Kecamatan Masaran, Kabupaten Sragen 57282",
         "description": "Pusat pembinaan kader dan pendidikan Islam dengan penekanan pada tahfiz Al-Qur'an dan pembentukan karakter."},
        {"name": "SD Muhammadiyah Terpadu Masaran", "category": "pendidikan",
         "address": "Masaran RT 27/RW 10, Kecamatan Masaran, Kabupaten Sragen 57282"},
        {"name": "MI Muhammadiyah Sidodadi", "category": "pendidikan",
         "address": "Desa Sidodadi, Kecamatan Masaran, Kabupaten Sragen 57282"},
        {"name": "MI Muhammadiyah Kliwonan", "category": "pendidikan",
         "address": "Dukuh Beku, Desa Kliwonan, Kecamatan Masaran, Kabupaten Sragen 57282"},
        {"name": "MI Muhammadiyah Pilang", "category": "pendidikan",
         "address": "Pilang RT 17/RW 04, Desa Pilang, Kecamatan Masaran, Kabupaten Sragen 57282"},

        # --- PAUD 'Aisyiyah (13 lembaga) ---
        {"name": "KB Aisyiyah Masaran", "category": "pendidikan",
         "address": "Jl. Kelapa No. 10, RT 30 RW 10, Masaran, Kecamatan Masaran, Kabupaten Sragen"},
        {"name": "TK Aisyiyah Masaran II", "category": "pendidikan",
         "address": "Jl. Kelapa No. 10, RT 30 RW 10, Masaran, Kecamatan Masaran, Kabupaten Sragen"},
        {"name": "TK Aisyiyah Masaran I", "category": "pendidikan",
         "address": "Jl. Murai, Rejowinangun, Masaran, Kabupaten Sragen"},
        {"name": "TK Aisyiyah II Krebet", "category": "pendidikan",
         "address": "Dukuh Kedungbulus, Desa Krebet, Kecamatan Masaran, Kabupaten Sragen"},
        {"name": "TK Aisyiyah Karangmalang", "category": "pendidikan",
         "address": "Jl. Raya Sragen–Solo Km. 13, Desa Karangmalang, Kecamatan Masaran, Kabupaten Sragen"},
        {"name": "BA Aisyiyah II Sepat", "category": "pendidikan",
         "address": "Desa Sepat RT 31, Kecamatan Masaran, Kabupaten Sragen"},
        {"name": "TK Aisyiyah Sidodadi", "category": "pendidikan",
         "address": "Kedungrejo RT 37, Desa Sidodadi, Kecamatan Masaran, Kabupaten Sragen"},
        {"name": "TK Aisyiyah III Sepat", "category": "pendidikan",
         "address": "Wonorejo RT 11, Desa Sepat, Kecamatan Masaran, Kabupaten Sragen"},
        {"name": "BA Aisyiyah I Krebet", "category": "pendidikan",
         "address": "RT 12 RW 04, Desa Krebet, Kecamatan Masaran, Kabupaten Sragen"},
        {"name": "TK Aisyiyah Jirapan", "category": "pendidikan",
         "address": "Dukuh Tompe RT 16, Desa Jirapan, Kecamatan Masaran, Kabupaten Sragen"},
        {"name": "TK Aisyiyah I Sepat", "category": "pendidikan",
         "address": "Dukuh Pucuk RT 13, Desa Sepat, Kecamatan Masaran, Kabupaten Sragen"},
        {"name": "TK Aisyiyah Pilang", "category": "pendidikan",
         "address": "Dukuh Jantran RT 27 RW 05, Desa Pilang, Kecamatan Masaran, Kabupaten Sragen"},
        {"name": "BA Aisyiyah Kliwonan", "category": "pendidikan",
         "address": "Dukuh Beku RT 19, Desa Kliwonan, Kecamatan Masaran, Kabupaten Sragen"},

        # --- Pendidikan nonformal ---
        {"name": "Rumah Tahfidz Daarul Arqom Muhammadiyah Masaran", "category": "pendidikan"},
        {"name": "Sekolah Lansia Aisyiyah Masaran", "category": "sosial"},

        # --- Masjid ---
        {"name": "Masjid Amanah", "category": "lainnya"},

        # --- AUM afiliasi & ekonomi ---
        {"name": "BMT HIRA", "category": "ekonomi", "description": "AUM afiliasi."},
        {"name": "BMT AMANAH", "category": "ekonomi", "description": "AUM afiliasi."},
        {"name": "Airmu", "category": "ekonomi"},
        {"name": "MBG PCM Masaran", "category": "ekonomi"},
    ],

    "berita": [
        # {"title": "", "content": "", "image": "", "published_at": "2026-10-01T09:00"},
    ],
    "kegiatan": [
        # {"title": "", "description": "", "location": "", "start_date": "2026-12-01T08:00", "end_date": "", "image": ""},
    ],

    "tautan": [
        {"title": "PP Muhammadiyah", "url": "https://muhammadiyah.or.id", "description": ""},
        # TODO: tambahkan website resmi PDM Kabupaten Sragen dan PWM Jawa Tengah
        # setelah kamu pastikan URL-nya benar-benar bisa dibuka.
    ],
}


# ---------------------------------------------------------------------------
# Tambahan dari "Rancangan Profil PCM Masaran" (diproses setelah DATA di atas)
# ---------------------------------------------------------------------------
DATA["profil"]["description"] += (
    "\n\n"
    "Kaderisasi dilakukan melalui tujuh Organisasi Otonom (Ortom): 'Aisyiyah, "
    "Pemuda Muhammadiyah, Nasyiatul 'Aisyiyah, Ikatan Pelajar Muhammadiyah (IPM), "
    "Hizbul Wathan, Tapak Suci Putera Muhammadiyah, dan Komando Kesiapsiagaan "
    "Angkatan Muda Muhammadiyah (KOKAM).\n\n"
    "Sepuluh majelis yang membantu pimpinan: Majelis Pembina Kesehatan Umum dan "
    "Pelayanan Sosial; Pembinaan Kader dan Sumber Daya Insani; Pendayagunaan Wakaf; "
    "Ekonomi dan Kewirausahaan; Pustaka dan Informasi; Pendidikan Dasar, Menengah, "
    "dan Pendidikan Nonformal; Pemberdayaan Masyarakat; Tabligh, Tarjih, dan Tajdid; "
    "Lingkungan Hidup; serta Hukum, HAM, dan Lembaga Bantuan Hukum.\n\n"
    "Lembaga yang membantu pimpinan: Lembaga Pembinaan Haji dan Umrah; Pembinaan dan "
    "Pengawasan Keuangan; Pengembangan Pesantren Muhammadiyah; Pengembangan Cabang, "
    "Ranting, dan Pembinaan Masjid; Hikmah dan Kebijakan Publik; LAZISMU; serta "
    "Seni, Budaya, dan Olahraga Pembinaan Angkatan Muda Muhammadiyah dan Ortom.\n\n"
    "Program rutin: Pengajian Ahad Pagi, pengajian guru dan karyawan, pengajian "
    "tingkat ranting, dan Sekolah Lansia."
)

DATA["amal_usaha"] += [
    {"name": "Komunitas Fotografi", "category": "lainnya"},
    {"name": "JagalMu", "category": "lainnya"},
    {"name": "BikersMu", "category": "lainnya"},
]

_DESKRIPSI = {
    "SMP Muhammadiyah 2 Masaran": "Membentuk peserta didik berkarakter Islami, berprestasi, kreatif, dan memiliki kemampuan akademik yang kompetitif.",
    "MTs Muhammadiyah 3 Masaran": "Madrasah yang mengintegrasikan pendidikan umum dan agama Islam untuk mencetak generasi cerdas, religius, dan berakhlak mulia.",
    "SD Muhammadiyah Terpadu Masaran": "Pembelajaran terpadu yang menggabungkan pendidikan umum, pendidikan agama, dan pembentukan karakter sejak dini.",
    "MI Muhammadiyah Sidodadi": "Pendidikan dasar yang menanamkan nilai keislaman, kedisiplinan, dan kecintaan terhadap ilmu pengetahuan.",
    "MI Muhammadiyah Kliwonan": "Membangun peserta didik yang beriman, cerdas, kreatif, dan peduli sosial melalui pembelajaran inovatif.",
    "MI Muhammadiyah Pilang": "Mengintegrasikan pendidikan agama dan ilmu umum untuk mencetak generasi muslim yang unggul, mandiri, dan berakhlak mulia.",
    "Rumah Tahfidz Daarul Arqom Muhammadiyah Masaran": "Pendidikan nonformal tahfiz Al-Qur'an di kompleks Balai Muhammadiyah Masaran.",
    "Sekolah Lansia Aisyiyah Masaran": "Program pendidikan nonformal dan pembinaan keagamaan bagi lansia.",
    "Masjid Amanah": "Masjid Muhammadiyah di kompleks Balai Muhammadiyah Masaran.",
}
for _aum in DATA["amal_usaha"]:
    if _aum["name"] in _DESKRIPSI and not _aum.get("description"):
        _aum["description"] = _DESKRIPSI[_aum["name"]]
    elif _aum["name"].startswith(("KB ", "TK ", "BA ")) and not _aum.get("description"):
        _aum["description"] = "Pendidikan anak usia dini di bawah naungan PCM dan PCA Masaran."
    elif _aum["name"] in ("Komunitas Fotografi", "JagalMu", "BikersMu"):
        _aum["description"] = "Komunitas binaan PCM Masaran."

