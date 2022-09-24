import { upload } from 'youtube-videos-uploader' //Typescript

const credentials = { email: 'email', pass: 'pass', recoveryemail: 'recoveryemail' }


const onVideoUploadSuccess = (videoUrl) => {
    console.log("Successfully uploaded video: " + videoUrl);
}
const video = { path: 't.mp4', title: 'Coldest Anime Moments 🥶 #badassanime #anime #animeedit #shorts #LostreakChicken #topanime #bestanime', description: 'Coldest Anime Moments 🥶 #badassanime #anime #animeedit #shorts #LostreakChicken #topanime #bestanime', language: 'english', tags: ['shorts', 'bestanime', 'topanime', 'animeedit', 'anime', 'LostreakChicken'], onSuccess:onVideoUploadSuccess, skipProcessingWait: true, onProgress: (progress) => { console.log('progress', progress) } }

upload(credentials, [video]).then(console.log)