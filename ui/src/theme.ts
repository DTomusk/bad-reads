import { createTheme } from "@mantine/core";

export const theme = createTheme({
  fontFamily: 'Inter, sans-serif',
  fontFamilyMonospace: 'JetBrains Mono, monospace',
  headings: {
    fontFamily: 'Noto Serif, serif',
    fontWeight: '700',
  },
  primaryColor: 'orange',
  colors: {
    orange: [
      '#FFF3E0', // 0 - lightest
      '#FFE0B2', // 1
      '#FFCC80', // 2
      '#FFB74D', // 3
      '#FFA726', // 4
      '#FF9800', // 5 - primary
      '#FB8C00', // 6
      '#F57C00', // 7
      '#EF6C00', // 8
      '#E65100', // 9 - darkest
    ],
  },
  defaultRadius: 'md',
  black: '#000000',
  white: '#FFFFFF',
  components: {
    AppShell: {
      styles: {
        main: {
          background: '#1a1a1a',
          color: '#FFFFFF',
        },
      },
    },
  },
});
