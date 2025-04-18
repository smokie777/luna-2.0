export const foo = () => {};

// this function was generated by chatgpt and also has a copy in /python
export const convertTimeHmsStringToMs = (str:string) => {
  const regex = /(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?/;
  const match = str.match(regex);
  
  if (!match) {
    throw new Error(`Cannot convert hms string "${str}" to ms!`);
  }

  const hours = parseInt(match[1]) || 0;
  const minutes = parseInt(match[2]) || 0;
  const seconds = parseInt(match[3]) || 0;  

  const ms = ((hours * 60 + minutes) * 60 + seconds) * 1000;

  if (ms > 86400000) {
    throw new Error('Cannot exceed a total time greater than one day.');
  }

  return ms;
};

// and this one too!
export const convertMsToHms = (ms: number) => {
  if (ms > 86400000) {
    throw new Error('Cannot exceed a total time greater than one day.');
  }
  
  let seconds = Math.floor(ms / 1000);
  let minutes = Math.floor(seconds / 60);
  const hours = Math.floor(minutes / 60);

  seconds = seconds % 60;
  minutes = minutes % 60;

  return { h: hours, m: minutes, s: seconds };
};

export const getRandomNumberBetween = (min: number, max: number) => Math.random() * (max - min) + min;

export const extractFirst7tvEmote = (s:string, emotesNameToUrlMap: Record<string, string>) => {
  const words = s.split(' ');
  for (let i = 0; i < words.length; i++) {
    if (emotesNameToUrlMap.hasOwnProperty(words[i])) {
      return words[i];
    }
  }
  return '';
};
