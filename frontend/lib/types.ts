export type TeamSummary = {
  name: string;
  systemStyle: string;
  championships: number;
  playoffAppearances: number;
  legacyScore: number;
  hallOfFamers: number;
};

export type SeasonTimelineEntry = {
  year: number;
  champion: string;
  finalsMatchup: string;
  mvp: string;
  keyStorylines: [string, string];
};
