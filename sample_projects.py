"""
Curated sample capstone projects for instant 1-click testing in VivaShield.
These mimic real-world engineering final-year projects with typical student architecture shortcuts.
"""

SAMPLE_PROJECTS = {
    "agri_iot": {
        "title": "AgriPulse: IoT Soil Sensor & CNN Leaf Disease Detection",
        "tech_stack": "Python, Flask, PyTorch (ResNet-18), ESP32, MQTT, SQLite",
        "category": "IoT & Deep Learning",
        "abstract": (
            "An automated crop monitoring system combining ESP32 microcontrollers deployed in fields "
            "with a cloud-based leaf disease diagnosis pipeline. Soil moisture, temperature, and humidity "
            "are streamed via MQTT to a Flask backend. Farmers upload leaf images via a mobile web app, "
            "which are classified into 14 disease classes using a fine-tuned ResNet-18 model trained on PlantVillage. "
            "Alerts are sent via Twilio SMS when moisture drops below threshold or disease confidence exceeds 85%."
        ),
        "code_snippet": (
            "# In app.py - Image classification endpoint\n"
            "@app.route('/predict', methods=['POST'])\n"
            "def predict():\n"
            "    img_file = request.files['image']\n"
            "    img = Image.open(img_file).convert('RGB')\n"
            "    tensor = transform(img).unsqueeze(0)\n"
            "    with torch.no_grad():\n"
            "        output = model(tensor)\n"
            "        prob, pred = torch.max(F.softmax(output, dim=1), 1)\n"
            "    # Save prediction directly into SQLite database without indexing\n"
            "    db.execute('INSERT INTO logs (user_id, disease, conf) VALUES (?, ?, ?)', \n"
            "               (request.form['user_id'], classes[pred], float(prob)))\n"
            "    return jsonify({'disease': classes[pred], 'confidence': float(prob)})\n"
        ),
        "typical_shortcuts": [
            "Trained and evaluated on clean PlantVillage lab photos; fails in real outdoor lighting/angles.",
            "SQLite used in a multi-user IoT application where concurrent MQTT writes cause database locks.",
            "ESP32 code hardcodes WiFi credentials in plain text firmware.",
            "No data augmentation or dropout used in transfer learning; potential overfitting."
        ]
    },
    "fintech_microservices": {
        "title": "PayFlow: Microservices Peer-to-Peer Payment Gateway",
        "tech_stack": "Node.js (Express), Go, Apache Kafka, PostgreSQL, Redis, Docker, JWT",
        "category": "Fintech & Distributed Systems",
        "abstract": (
            "A distributed peer-to-peer wallet and payment processing engine. Features an Auth Service (Node.js/JWT), "
            "a Wallet Ledger Service (Go), and a Notification Service (Python). When a transaction is initiated, "
            "the Wallet Service writes a pending ledger entry, publishes a 'transaction.created' event to Kafka, "
            "and locks the sender wallet balance in Redis for 30 seconds to prevent double-spending. "
            "If downstream payment confirmation fails, a compensating transaction is executed to unlock funds."
        ),
        "code_snippet": (
            "// Go Wallet Service - Process Transfer\n"
            "func Transfer(senderId, receiverId string, amount float64) error {\n"
            "    // Acquire Redis mutex lock\n"
            "    lockKey := fmt.Sprintf(\"lock:wallet:%s\", senderId)\n"
            "    acquired, err := redisClient.SetNX(ctx, lockKey, 1, 30*time.Second).Result()\n"
            "    if !acquired { return errors.New(\"transaction in progress\") }\n"
            "    \n"
            "    // Deduct and credit in PostgreSQL\n"
            "    tx := db.Begin()\n"
            "    tx.Exec(\"UPDATE wallets SET balance = balance - ? WHERE id = ?\", amount, senderId)\n"
            "    tx.Exec(\"UPDATE wallets SET balance = balance + ? WHERE id = ?\", amount, receiverId)\n"
            "    tx.Commit()\n"
            "    \n"
            "    // Publish event to Kafka topic\n"
            "    kafkaProducer.Produce(&kafka.Message{TopicPartition: kafka.TopicPartition{Topic: &topic}, Value: payload})\n"
            "    return nil\n"
            "}\n"
        ),
        "typical_shortcuts": [
            "Dual-write problem: Database transaction commits before Kafka publish; if Kafka crashes after commit, event is lost (violates 2PC/Outbox pattern).",
            "Redis distributed lock doesn't handle lock expiration during long database hangs (split-brain).",
            "Floating point `float64` used for money instead of integer cents / decimal (IEEE 754 precision errors).",
            "JWT token revocation is not implemented; stolen tokens remain valid until expiration."
        ]
    },
    "healthcare_web3": {
        "title": "MedVault: Decentralized Electronic Health Records on IPFS",
        "tech_stack": "Solidity (Ethereum/Polygon), React, Web3.js, IPFS, AES-256-GCM, Express",
        "category": "Web3 & Healthcare Security",
        "abstract": (
            "A patient-centric electronic health record management system ensuring HIPAA compliance and data integrity. "
            "Medical records, MRI scans, and prescriptions are symmetrically encrypted locally using AES-256-GCM before "
            "being pinned to IPFS. The IPFS Content Identifier (CID) and decryption key access permissions are stored "
            "on a Polygon smart contract. Patients grant time-bounded viewing access to doctors by encrypting the AES key "
            "with the doctor's public RSA key and storing the permission on-chain."
        ),
        "code_snippet": (
            "// Solidity Smart Contract snippet\n"
            "contract MedVault {\n"
            "    struct Record {\n"
            "        string ipfsHash;\n"
            "        uint256 timestamp;\n"
            "        address uploader;\n"
            "    }\n"
            "    mapping(address => Record[]) private patientRecords;\n"
            "    mapping(address => mapping(address => bool)) public doctorAccess;\n"
            "    \n"
            "    function addRecord(string memory _hash) public {\n"
            "        patientRecords[msg.sender].push(Record(_hash, block.timestamp, msg.sender));\n"
            "    }\n"
            "    \n"
            "    function grantAccess(address _doctor) public {\n"
            "        doctorAccess[msg.sender][_doctor] = true;\n"
            "    }\n"
            "}\n"
        ),
        "typical_shortcuts": [
            "Gas fees scale quadratically when returning dynamic arrays from smart contracts.",
            "Smart contract stores `grantAccess` boolean but lacks expiration timestamps or granular record revocation.",
            "IPFS pin relies on a centralized Infura/Pinata gateway; if unpinned, patient medical files vanish.",
            "AES keys stored temporarily in browser localStorage (vulnerable to XSS attacks)."
        ]
    }
}
