import { createTheme } from "@mantine/core";

export const theme = createTheme({
  fontFamily: 'Inter, sans-serif',
  fontFamilyMonospace: 'JetBrains Mono, monospace',
  headings: {
    fontFamily: 'Noto Serif, serif',
    fontWeight: '700',
  },
  primaryColor: 'teal',
  autoContrast: true,
  colors: {
    teal: [
      '#197278', // 0 - base
      '#17686e', // 1
      '#155e64', // 2
      '#13545a', // 3
      '#114a50', // 4
      '#0f4046', // 5
      '#0d363c', // 6
      '#0b2c32', // 7
      '#092228', // 8
      '#07181e', // 9 - darkest
    ],
    dark: [
      '#2a3d3c', // 0 - lightest
      '#273938', // 1
      '#243534', // 2
      '#213130', // 3
      '#1e2d2c', // 4
      '#1b2928', // 5
      '#203130', // 6 - original dark.0
      '#1c2c2c', // 7
      '#182828', // 8
      '#142424', // 9 - darkest
    ],
    light: [
      '#f9f4f1', // 0 - base
      '#f5f0ed', // 1
      '#f1ece9', // 2
      '#ede8e5', // 3
      '#e9e4e1', // 4
      '#e5e0dd', // 5
      '#e1dcd9', // 6
      '#ddd8d5', // 7
      '#d9d4d1', // 8
      '#d5d0cd', // 9 - darkest
    ],
    secondary: [
      '#8c362b', // 0 - base
      '#7e3027', // 1
      '#702a23', // 2
      '#62241f', // 3
      '#541e1b', // 4
      '#461817', // 5
      '#381213', // 6
      '#2a0c0f', // 7
      '#1c060b', // 8
      '#0e0007', // 9 - darkest
    ],
    highlight: [
      '#cf5c4f', // 0 - base
      '#ba5347', // 1
      '#a54a3f', // 2
      '#904137', // 3
      '#7b382f', // 4
      '#662f27', // 5
      '#51261f', // 6
      '#3c1d17', // 7
      '#27140f', // 8
      '#120b07', // 9 - darkest
    ],
  },
  defaultRadius: 'md',
  black: '#000000',
  white: '#FFFFFF',
  components: {
    Text: {
      defaultProps: {
        c: '#FFFFFF',
      },
    },
    Title: {
      defaultProps: {
        c: '#FFFFFF',
      },
    },
    Button: {
      defaultProps: {
        c: 'white',
        shadow: 'xl',
      },
    },
    Divider: {
      defaultProps: {
        color: 'white',
        size: 'sm',
      },
    },
    Paper: {
      defaultProps: {
        bg: 'rgba(0, 0, 0, 0)',
        c: 'white',
      },
    },
  },
});
