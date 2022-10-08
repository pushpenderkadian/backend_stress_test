import { io } from "socket.io-client";
import axios from 'axios';
import { sha256 } from "js-sha256";

const sha256toNumber = (name) => {
    const hashedName = sha256(name);
    const splicedHash = hashedName.slice(0, 8);
    return parseInt(splicedHash, 16);
};

const sockets = {}

const connectSocket = async (i=0) => {

    const response = await axios({
        url: "https://auth.api.edvora.me/login",
        method: "POST",
        data: {
            username: "vegeta" + i,
            password: "00",
        }
    })
    if (response?.data) {
        const data = response.data;
        let socket;

        socket = io('https://in01.srv.edvora.me/', {
            transports: ["websocket"],
            auth: {
                Authorization: btoa(
                    JSON.stringify({
                        token: data.token,
                        username: data.username,
                        organization_id: data.organization_id,
                        session_id: data.session_id,
                        role_id: data.role_id,
                        uid: sha256toNumber(data.username),
                    })
                ),
                room_id: "632947bf190b14f5f571bda3"
            },
        });

        socket.on("connect", () => {
            console.log("SOCKET CONNECTED", socket.connected, socket.id, data.username);
            sockets[data.username] = { data, socket, metadata: null, connected: false }
            socketListeners(socket)
            getRoomMetadata(socket, "632947bf190b14f5f571bda3");
        });

        socket.on("room_metadata", (metadata) => {
            sockets[data.username]["metadata"] = metadata
            const connected = sockets[data.username]["connected"]
            if (!(sha256toNumber(data.username) in metadata.users_in_meeting) && !connected) connectMeeting(socket, data, metadata)
        });

        socket.on("connect_error", (err) => {
            console.log(err, Object.keys(err), err.type, err.message, err.description);
        });

        socket.io.on("reconnect", (attempt) => {
            console.log("reconnected", attempt);

            // socket.emit("sync",
            //     {
            //         room_id: '632947bf190b14f5f571bda3',
            //         uid : sha256toNumber(data.username),
            //         meeting_id: sockets[data.username]["metadata"]["meeting_id"],
            //         connect_type: 0,
            //         raise_hand: false
            //     }
            // );
        });

        socket.on("disconnect", (reason) => {
            console.log("socket disconnected", reason)
        });

        socket.on("added_to_room", (data) => {
            console.log('added_to_room', data)
            if (i<100) {
                connectSocket(i+1)
            }
        });
    }

}

connectSocket();

const connectMeeting = (socket, data, metadata) => {
    socket.emit("connect_meeting", { room_id: metadata.room_id, reconnecting: false, meeting_id: metadata.meeting_id });
    sockets[data.username]["connected"] = true
}	

const getRoomMetadata = (socket, room_id) => {
    socket.emit("get_room_metadata", { room_id });
};

const socketListeners = (socket) => {
    socket.on("room_metadata", (data) => {
        //console.log('room_metadata')
    });

    socket.on("added_to_lobby", (data) => {
        console.log("added_to_lobby")
    });

    socket.on("user_kicked_out", (data) => {
        console.log('user_kicked_out')
    });

    socket.on("user_entered_room", (data) => {
        //console.log('user_entered_room', data)
    });

    socket.on("user_left_room", (data) => {
        console.log('user_left_room')
    });

    socket.on("requested_to_join", (data) => {
        console.log('requested_to_join')
    });

    socket.on("user_left_lobby", (data) => {
        console.log('user_left_lobby')
    });

    socket.on("rejected_by_host", (data) => {
        console.log('rejected_by_host')
    });

    socket.on("you_have_been_kicked_out", (data) => {
        console.log('you_have_been_kicked_out')
    });

    socket.on("end_meeting", (data) => {
        console.log('end_meeting')
    });

    //chat events
    socket.on("chat_message", (data) => {
        console.log('chat_message')
    });

    socket.on("all_chats", (data) => {
        console.log('all_chats')
    });

    //announcement
    socket.on("announcement", (data) => {
        console.log("announcement")
    });

    socket.on("mute_myself", async (data) => {
        console.log('mute_myself', data)
    });

    socket.on("recording_meet_start", (data) => {
        console.log('recording_meet_start')
    });

    socket.on("recording_meet_end", (data) => {
        console.log('recording_meet_end')
    });

    socket.on("list_sid", (data) => {
        console.log('list sid')
    });

    socket.on("room_noexist", (data) => {
        console.log('room_noexist')
    })

    socket.on("logger", (data) => {
        //console.log('logger', data)
    });

    socket.onAny((eventName, ...args) => {
        //console.log("EVENT:", eventName, ...args);
    });
};