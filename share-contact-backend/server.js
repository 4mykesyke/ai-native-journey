import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { Twilio } from 'twilio';

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const client = new Twilio(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);

app.post('/send-whatsapp', async (req, res) => {
  const { to, message } = req.body;
  try {
    const msg = await client.messages.create({
      from: process.env.TWILIO_WHATSAPP_NUMBER,
      to: `whatsapp:${to}`,
      body: message,
    });
    res.json({ success: true, sid: msg.sid });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
});

app.post('/send-sms', async (req, res) => {
  const { to, message } = req.body;
  try {
    const msg = await client.messages.create({
      from: process.env.TWILIO_SMS_NUMBER,
      to,
      body: message,
    });
    res.json({ success: true, sid: msg.sid });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
});

app.get('/', (req, res) => {
  res.send('Share Contact Backend is running!');
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`Backend running on http://localhost:${PORT}`)); 